Title: Subscription tokens
Slug: subscription-tokens


Historically, it has been impossible to know how many people have subscribed to a podcast. This makes it impossible to reliably distinguish one media download from another, when coming from the same network, or whether a download on one device was started along with another on a different device, by the same user.

DotPodcast solves this problem by creating a pseudonymised subscription system, that identifies a listener to a specific podcast, so that their downloads can be distinguished from other listeners, but does not share information across podcasts.

The following is a comprehensive description of the system, from end to end. Guides are also available, with more domain-specific information for:

- [podcast hosting service providers](hosting-services)
- [podcast directory developers](directories)
- [podcast player (or "podcatcher") developers](apps)

## Generating a subscription token

There are three types of subscription tokens that can be generated:
- [preview tokens](#preview-tokens)
- [download tokens](#download-tokens)
- [transit tokens](#transit-tokens)

### Preview tokens

A preview token is required for podcast directories that want to allow episodes to be played via a podcast's landing or listing page. The same content is delivered when a listener previews the episode, but the hosting service is able to determine the behaviour so that it can be reflected adequately in analytics.

#### Obtaining a preview token

A token is obtained by calling a podcast's subscription URL via an HTTP POST containing a subscriber hash and optional information. For example:

```
POST /dp-subscribe/ HTTP/1.1
Host: thedotpodcastshow.com
Content-Type: application/json

{
    "app_name": "DotPodcast Directory",
    "app_url": "https://directory.dotpodcast.org/",
    "token_kind": "preview"
}
```

The `app_url` value distinguishes the app or directory service from other such consumers and is used when generating a JSON Web Token for downloading episodes. The `token_type` (which must be set, and equal `"preview"`) instructs the server which type of token to expect. The `app_name` value is optional.

The hosting provider will return a JSON object in the following form:

```json
{
    "preview_secret": "a7K9N7ye2K3VpPVq7hZAfXhMYJKMtkQOAWXzWeYT15KLon209zpuT5jfY2QE4sz2"
}
```

The directory service stores the secret for later use.

### Download tokens

Download tokens are obtained by podcast players, and are bound to a specific user of a podcast app.

#### Obtaining a download token

A token is obtained by calling a podcast's subscription URL via an HTTP POST containing a subscriber hash and optional information. For example:

```
POST /dp-subscribe/ HTTP/1.1
Host: thedotpodcastshow.com
Content-Type: application/json

{
    "app_name": "DotPodcast Player",
    "app_url": "https://player.dotpodcast.org/",
    "app_logo": "https://player.dotpodcast.org/img/logo.svg",
    "token_kind": "download",
    "subscriber_hash": "eae950252dec7434b6d98d16dfc8dbd63552ba27",
    "subscriber_details": {
        "country": "United States",
        "city": "New York, NY",
        "platform": "ios",
        "device_type": "phone",
        "device_name": "iPhone X"
    }
}
```

The `app_url` value is required, as it is used for generating a JSON Web Token for downloading episodes.

The `app_name` and `app_logo` values are optional but recommended for allowing hosting services to identify an app within their analytics dashboard.

The `token_type` must be set, and equal to `"download"`.

The `subscriber_hash` value should be an SHA256 string made up of information that uniquely identifies the user and app, for example: the public key of the user and the URL to the app, joined via a single space. Alternatively, an app may generate uniquely-identifiable IDs for its users.

Podcast hosting providers should enforce regular expression checking on the hash, to ensure that a valid value has been generated. An example regular expression for an SHA256 string is `[A-Fa-f0-9]{64}`, and reject requests containing hash strings that don't conform. This will help regulate behaviour among app developers and hosting providers.

The `subscriber_details` object should contain the above information, but nothing that is identifiable to the app user.

The hosting provider will return a JSON object in the following form:

```json
{
    "subscriber_hash": "eae950252dec7434b6d98d16dfc8dbd63552ba27",
    "subscriber_secret": "9hU9ikElLJsNAKf9qnkbfAdSSszdLHQECdGP6CWzo3lSSICvwiZnNTfjIthppOIr"
}
```

The podcast player stores the secret for later use.

---

Once a preview or download token (a subscription token) has been generated, it can be used when requesting the download of a piece of podcast content. See [Requesting content](../requesting-content).

### Transit tokens

A transit token is a way of identifying one hosting service from another, so that users can move between providers easily, and so that when an incoming provider obtains content to move it to their own storage, the download is not tracked and added to analytics.

Specifications for transit tokens are coming soon.
