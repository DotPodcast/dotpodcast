Title: Requesting content
Slug: requesting-content


When a [subscription token](../subscription-tokens) has been obtained by an app or directory service for a specific podcast, it can be used to request the audio/video content of a podcast feed.

The `content_audio` or `content_video` objects within a feed provide a thin API endpoint that allows content to be securely redeemed.

There are four main types of content request:

- [preview requests](#preview-requests)
- [standard content requests](#standard-content-requests)
- [restricted content requests](#restricted-content-requests)
- [export requests](#export-requests)

## Preview requests

A podcast directory or app uses preview requests to swap a preview token for a URL to a piece of audio or video. This is done by appending a JSON Web Token to the URL specified in the `content_audio` or `content_videos`'s `url` property. The unencrypted JSON string looks like this:

```json
{
    "iss": "DotPodcast Player",
    "iat": 1508170987,
    "exp": 1539706987,
    "aud": "https://player.dotpodcast.co/",
    "sub": "preview",
    "content_id": "http://thedotpodcastshow.com/episode-1/"
}
```

The `sub` value must be set to `"preview"`, and the `content_id` must point to the ID of the episode as set out in the feed item.

It is HS256-encrypted with the `preview_secret` retrieved when obtaining the preview token, and appended to a GET request, like so:

```
GET /dp-download/?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJEb3RQb2RjYXN0IFBsYXllciIsImlhdCI6MTUwODE3MDk4NywiZXhwIjoxNTM5NzA2OTg3LCJhdWQiOiJodHRwczovL3BsYXllci5kb3Rwb2RjYXN0Lm9yZy8iLCJzdWIiOiJwcmV2aWV3In0.4H_xKNE-YkJTj0B-L_3VBwawGCsaKhraxS2C4enMm3I HTTP/1.1
Host: thedotpodcastshow.com
Content-Type: application/json
```

Once the API endpoint has been called successfully, the server can respond in one of three ways. Either with a 301 redirect to the audio/video content, a JSON response like so:

```json
{
    "url": "http://a-long-s3like.url?with=shortlived-token",
    "mime_type": "audio/mpeg",
    "file_size": 14400000
}
```

...or directly with the file encoded in the body, provided that the MIME type of the response exactly matches that specified in the `content_audio` or `content_video` object.

App or directory developers should expect and cater for all three forms of response.


## Standard content requests

A podcast app uses standard content requests to swap a download token for a URL to a piece of audio or video. This is done by appending a JSON Web Token to the URL specified in the `content_audio` or `content_videos`'s `url` property. The unencrypted JSON string looks like this:

```json
{
    "iss": "DotPodcast Player",
    "iat": 1508170987,
    "exp": 1539706987,
    "aud": "https://player.dotpodcast.co/",
    "sub": "preview",
    "content_id": "http://thedotpodcastshow.com/episode-1/"
}
```

The `sub` value must be set to the `subscriber_hash` that was originally sent to the encryption endpoint. The `content_id` must point to the ID of the episode as set out in the feed item.

It is then HS256-encrypted with the `subscriber_secret` retrieved when obtaining the download token, and appended to a GET request, like so:

```
GET /dp-download/?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJEb3RQb2RjYXN0IFBsYXllciIsImlhdCI6MTUwODE3MDk4NywiZXhwIjoxNTM5NzA2OTg3LCJhdWQiOiJodHRwczovL3BsYXllci5kb3Rwb2RjYXN0Lm9yZy8iLCJzdWIiOiJlYWU5NTAyNTJkZWM3NDM0YjZkOThkMTZkZmM4ZGJkNjM1NTJiYTI3In0.6yAklBB7dzrsjXKFw3z3rjSGIFSA07W4HzWd7DBrlNc HTTP/1.1
Host: thedotpodcastshow.com
Content-Type: application/json
```

Once the API endpoint has been called successfully, the server can respond in one of three ways. Either with a 301 redirect to the audio/video content, a JSON response like so:

```json
{
    "url": "http://a-long-s3like.url?with=shortlived-token",
    "mime_type": "audio/mpeg",
    "file_size": 14400000
}
```

...or directly with the file encoded in the body, provided that the MIME type of the response exactly matches that specified in the `content_audio` or `content_video` object.

App or directory developers should expect and cater for all three forms of response.


## Restricted content requests

A podcast app uses restricted content requests to swap a download token for a URL to a piece of audio or video behind a Bitcoin paywall. This is done by appending a JSON Web Token to the URL specified in the `content_audio` or `content_videos`'s `url` property.

This is a multi-step process, as it involves transactions which cannot be tracked synchronously.

### Step 1: Perform the Bitcoin transaction

The podcast app is responsible for performing the Bitcoin transaction, by guiding the user through the process of transferring the specified amount of Bitcoin (specified in satoshi as per the spec) into the `bitcoin_address` associated with the piece of content. A transaction ID must be obtained and passed to the hosting service.

### Step 2: Passing the transaction ID to the hosting service

The app passes the transaction ID along with other key information to the hosting service, via a JSON Web Token. The unencrypted JSON string looks like this:

```json
{
    "iss": "DotPodcast Player",
    "iat": 1508170987,
    "exp": 1539706987,
    "aud": "https://player.dotpodcast.co/",
    "sub": "eae950252dec7434b6d98d16dfc8dbd63552ba27",
    "bitcoin_tx_id": "<bitcoin transaction id>",
    "restricted_content_id": "http://thedotpodcastshow.com/episode-1/ad-free/",
    "callback_url": "https://player.dotpodcast.co/dp-callback/?id=7b9cbac6-6193-4292-a2d8-0880a0a60aaf"
}
```

The `sub` value must be set to the `subscriber_hash` that was originally sent to the encryption endpoint. The `restricted_content_id` must point to the ID of the piece of restricted content, as specified in the feed.

The `bitcoin_tx_id` value refers to the ID of a recent Bitcoin transaction used to pay for the content. The podcast app is responsible for guiding the user through the Bitcoin transaction, but the podcast hosting service is strongly encouraged to verify the transaction on the blockchain.

The `callback_url` value must be provided since the Bitcoin transaction cannot be confirmed as part of the HTTP request-response cycle (there is a way to obtain the status of the content if the callback URL can't be accessed).

The JSON string is then HS256-encrypted with the `subscriber_secret` retrieved when obtaining the download token, and appended to a GET request, like so:

```
GET /dp-download/?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJEb3RQb2RjYXN0IFBsYXllciIsImlhdCI6MTUwODE3MDk4NywiZXhwIjoxNTM5NzA2OTg3LCJhdWQiOiJodHRwczovL3BsYXllci5kb3Rwb2RjYXN0Lm9yZy8iLCJzdWIiOiJlYWU5NTAyNTJkZWM3NDM0YjZkOThkMTZkZmM4ZGJkNjM1NTJiYTI3IiwiYml0Y29pbl90eF9pZCI6IjxiaXRjb2luIHRyYW5zYWN0aW9uIGlkPiIsImNhbGxiYWNrX3VybCI6Imh0dHBzOi8vcGxheWVyLmRvdHBvZGNhc3Qub3JnL2RwLWNhbGxiYWNrLz9pZD03YjljYmFjNi02MTkzLTQyOTItYTJkOC0wODgwYTBhNjBhYWYifQ.ennQTBu0j8U0_dEVS6wkRqNpcxBBcvaDF2gnV4Ol1no HTTP/1.1
Host: thedotpodcastshow.com
Content-Type: application/json
```

Upon successful completion of this step, the hosting service's API will respond with a ping URL, like so:

```json
{
    "restricted_content_id": "http://thedotpodcastshow.com/episode-1/ad-free/",
    "subscriber_hash": "eae950252dec7434b6d98d16dfc8dbd63552ba27",
    "ping_url": "http://thedotpodcastshow.com/dp-ping/"
}
```

### Step 3: Getting notified automatically when the content is available

Since Bitcoin transactions cannot be confirmed within the HTTP request-response cycle, the app will inform the user that the content will be made available soon (once the Bitcoin transaction has been confirmed and read by the hosting provider).

Once the Bitcoin transaction is confirmed by the hosting service, the service will perform an HTTP GET request to the `callback_url` provided, containing a JSON Web Token. The unencrypted JSON string will look like this:

```json
{
    "restricted_content_id": "http://thedotpodcastshow.com/episode-1/ad-free/",
    "subscriber_hash": "eae950252dec7434b6d98d16dfc8dbd63552ba27",
    "download_url": "http://a-long-s3like.url?with=shortlived-token",
    "mime_type": "audio/mpeg",
    "file_size": 14400000
}
```

The `restricted_content_id` value will match the same `id` of the requested piece of restricted content, as specified in the feed. The `subscriber_hash` is used to identify the specific user who requested the content`

The request will come in the following form:

```
GET /dp-callback/?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJEb3RQb2RjYXN0IFBsYXllciIsImlhdCI6MTUwODE3MDk4NywiZXhwIjoxNTM5NzA2OTg3LCJhdWQiOiJodHRwczovL3BsYXllci5kb3Rwb2RjYXN0Lm9yZy8iLCJzdWIiOiJlYWU5NTAyNTJkZWM3NDM0YjZkOThkMTZkZmM4ZGJkNjM1NTJiYTI3IiwiYml0Y29pbl90eF9pZCI6IjxiaXRjb2luIHRyYW5zYWN0aW9uIGlkPiIsImNhbGxiYWNrX3VybCI6Imh0dHBzOi8vcGxheWVyLmRvdHBvZGNhc3Qub3JnL2RwLWNhbGxiYWNrLz9pZD03YjljYmFjNi02MTkzLTQyOTItYTJkOC0wODgwYTBhNjBhYWYifQ.ennQTBu0j8U0_dEVS6wkRqNpcxBBcvaDF2gnV4Ol1no HTTP/1.1
Host: player.dotpodcast.co
```

The app will decrypt the token using the `subscriber_secret` obtained earlier, and download the content on behalf of the user, or send a push notification to that effect.

An extra step can be setup, should the callback URL fail.

### Step 4: Manually obtaining the status of restricted content

If the app's web server is unable to accept the request (ie: it's down at the time), the app can call the `ping_url` provided by the hosting service in step 2 to manually obtain the status of the current piece of content.

The app passes the original transaction ID along with other key information to the ping URL, via a JSON Web Token. The unencrypted JSON string looks like this:

```json
{
    "iss": "DotPodcast Player",
    "iat": 1508170987,
    "exp": 1539706987,
    "aud": "https://player.dotpodcast.co/",
    "sub": "eae950252dec7434b6d98d16dfc8dbd63552ba27",
    "bitcoin_tx_id": "<bitcoin transaction id>",
    "restricted_content_id": "http://thedotpodcastshow.com/episode-1/ad-free/"
}
```

The `sub` value must be set to the `subscriber_hash` that was originally sent to the encryption endpoint. The `bitcoin_tx_id` value refers to the ID of the Bitcoin transaction used to pay for the content.

The JSON string is then HS256-encrypted with the `subscriber_secret` and appended to a GET request, like so:

```
GET /dp-ping/?eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJEb3RQb2RjYXN0IFBsYXllciIsImlhdCI6MTUwODE3MDk4NywiZXhwIjoxNTM5NzA2OTg3LCJhdWQiOiJodHRwczovL3BsYXllci5kb3Rwb2RjYXN0Lm9yZy8iLCJzdWIiOiJlYWU5NTAyNTJkZWM3NDM0YjZkOThkMTZkZmM4ZGJkNjM1NTJiYTI3IiwiYml0Y29pbl90eF9pZCI6IjxiaXRjb2luIHRyYW5zYWN0aW9uIGlkPiIsImNvbnRlbnRfaWQiOiJodHRwOi8vdGhlZG90cG9kY2FzdHNob3cuY29tL2VwaXNvZGUtMS8ifQ.5bDeLZEB_8KAEMHSei1hdBybxUxeHoLnScokjN55A04 HTTP/1.1
Host: thedotpodcastshow.com
Content-Type: application/json
```

Once the ping URL has been called successfully, the server will respond with a JSON string, like so:

```json
{
    "restricted_content_id": "http://thedotpodcastshow.com/episode-1/ad-free/",
    "subscriber_hash": "eae950252dec7434b6d98d16dfc8dbd63552ba27",
    "download_url": "http://a-long-s3like.url?with=shortlived-token",
    "mime_type": "audio/mpeg",
    "file_size": 14400000
}
```

The app will then download the content on behalf of the user, or send a push notification to that effect.

## Export requests

Export requests allow hosting providers to download content from other providers, so that they can import content, allowing podcasters to easily move between providers.

More information on export requests are coming soon, but in broad terms, a transit token is requested when the incoming hosting service parses the feed of an existing podcast. This will involve some user interaction, and a similar flow to OAuth.

Once a valid transit token is obtained, a hosting service can use it to obtain original URLs to content stored on the outgoing host's infrastructure.
