Title: DotPodcast JSON feed specification v1
Date: 2017-10-12
Author: Mark
Slug: spec-v1
Summary: Version 1 of the DotPodcast JSON Feed spec


The DotPodcast JSON Feed spec is derived from the original [JSON Feed](https://jsonfeed.org/) spec, and makes no modifications to its structure. A sample, taken directly from their documentation looks like this:

```json
{
    "version": "https://jsonfeed.org/version/1",
    "title": "My Example Feed",
    "home_page_url": "https://example.org/",
    "feed_url": "https://example.org/feed.json",
    "items": [
        {
            "id": "2",
            "content_text": "This is a second item.",
            "url": "https://example.org/second-item"
        },
        {
            "id": "1",
            "content_html": "<p>Hello, world!</p>",
            "url": "https://example.org/initial-post"
        }
    ]
}
```

## Why JSON and not RSS?

XML (on which RSS is based) is slow and difficult to parse. New apps and services built around podcasting use it because it's what everyone uses, and moving people to another system is difficult, as the RSS spec (and its podcast-specific additions, provided by Apple) were built up over time.

But since DotPodcast is making fundamental changes to the way the entire podcasting ecosystem operates, it makes sense to adopt a more easily-parsable and human-readable syntax. And so, JSON Feed.

## The DotPodcast JSON Feed extension

The DotPodcast spec adds an extension called `_dotpodcast` to the header section (before the `items` list) and the `items` list itself. For example:

```json
{
    "version": "https://jsonfeed.org/version/1",
    "title": "My Example Feed",
    "home_page_url": "https://example.org/",
    "feed_url": "https://example.org/feed.json",
    "_dotpodcast": {
        "hosts": [
            {
                "name": "Geoff",
                "uri": "htto://example.com/hosts/geoff",
                "avatar": "htto://example.com/hosts/geoff.jpg"
            },
            {
                "name": "Sally",
                "uri": "htto://example.com/hosts/sally",
                "avatar": "htto://example.com/hosts/sally.jpg"
            }
        ]
    },
    "items": [
        {
            "id": "2",
            "content_text": "This is a second item.",
            "url": "https://example.org/second-item",
            "_dotpodcast": {
                "hosts": [
                    "htto://example.com/hosts/sally"
                ]
            }
        },
        {
            "id": "1",
            "content_html": "<p>Hello, world!</p>",
            "url": "https://example.org/initial-post",
            "_dotpodcast": {
                "hosts": [
                    "htto://example.com/hosts/geoff"
                ]
            }
        }
    ]
}
```

---

## The header object

The header `_dotpodcast` object is the one that appears before the list of items. It contains information about the podcast itself, that isn't covered by the JSON Feed spec. The `_podcast` extension object can contain the following:

- `version` (required, string) is the URL of the version of the format the feed uses. This is the version of the DotPodcast spec, not the
JSON Feed format. Example: _http://dotpodcast.org/spec-v1_.

- `subscription_url` (required, string) is the URL to the subscription endpoint, which is used to generate a subscription token that can be exchanged when downloading episodes. See [Subscription tokens](../subscription-tokens) for more information.

- `feed_title` (optional, string) is the title of the feed as it should appear in a podcast app or directory. This may be different from the name of the JSON Feed itself.

- `artwork` (optional but highly recommended, object) specifies the podcast cover artwork at varying sizes:
    - `@1x` (required, string) is the URL to a 1400x1400 image.
    - `@2x` (required, string) is the URL to a 2800x2800 image.
    - Any other sizes can be added here, that may be supported by third-party directories such as Apple Podcasts.

- `subtitle` (optional but recommended, string) is a short sentence that describes the podcast. For example, a podcast title might be "Beware of the Leopard", with a subtitle of "The Hitchhiker's Guide to the Galaxy podcast".

- `publisher` (optional, object) specifies information about the publisher of theh podcast (for example, NPR or Gimlet Media):
    - `name` (optional, string) is the publisher's name.
    - `url` (optional, string) is the URL of a site owned by the publisher. When publishing multiple podcasts under the same publisher, it is important to keep the URL the same, as this will become the unique identifier for that publisher, and will enable directories to find other podcasts by the same publisher.
    - `logo` (optional, string) is the URL to a logo for the publisher. It should be square and relatively large — such as 512x512 — and should use transparency where appropriate, since it may be rendered on a non-white background.

- `taxonomy_terms` (optional but recommended, array) is a collection of taxonomy term URIs that categorise the podcast. (See the [list of taxonomies](../taxonomies)).

- `description_html` (optional but recommended, string) is an HTML string that describes the podcast. It should be one or more paragraphs in length, optionally with links.

- `description_text` (optional but recommended, string) is a plain-text description of the podcast, for use in rendering summary cards or where a podcast app doesn't want to - or can't - provide an HTML description.

- `banner_image` (optional, string) is the URL of an image to use as a banner. Online directories will use this banner image when displaying the main landing page for a podcast. 1500x500 is the optional size for the image.

- `hosts` (optional, array) is an array of objects containing information about the podcast's host(s). It should contain
    - `name` (required, string): the full name of the host.
    - `uri` (required, string): a unique identifying address for the host (like their website or [Onename](https://onename.com/) profile page). It must be something that can identify the host across multiple podcasts running on multiple hosting services or provided via multiple networks, so must not be a page hosted by a particular podcast. It should be a URL that is not likely to change.
    - `avatar` (optional, string): the URL to an avatar image. This should be around 512x512, square and with no transparency or masks (ie: it should not be an image in a circle). This image does not have to be unique across podcasts or services.

### Why no language tag?

The spoken language used in the podcast should be added as a taxonomy term, as it may not always be relevant ( music podcasts with no presenters may have no spoken language, and some podcasts may even use multiple languages).

### Why no "explicit" tag?

Instead of marking a show as containing "explicit" language or not, podcasters are encouraged to use a taxonomy term that denotes the level of profanity being used.

---

## The item object

Each episode in the feed is represented by an object within the `items` array. as with the header object, all the pre-existing JSON Feed specs apply.  The `_podcast` extension object inside an item object can contain the following:

- `season_number` (optional, integer) is the season number of the podcast, if applicable. If not, the value should be omitted.

- `episode_number` (optional, integer) is the number of the episode within the season. If the podcast is not season-based, this value, along with `season_number` should be omitted.

- `subtitle` (optional, string) is a short sentence that describes the episode.

- `content_audio` (required if `content_video` is not supplied, object) describes the audio content file type and location:
    - `mime_type` (required, string) is the MIME type of the audio file (for example: `audio/mpeg`)
    - `url` (required, string) is the URL for the episode media file (known in RSS as the "enclosure")
    - `file_size` (required, integer) is the size, in bytes, of the file
    - `duration` (required, integer) is the duration (in total number of seconds) of the file

- `content_video` (required if `content_audio` is not supplied, object) describes the video content file type and location:
    - `mime_type` (required, string) is the MIME type of the video file (for example: `video/mpeg`)
    - `url` (required, string) is the URL for the episode media file (known in RSS as the "enclosure")
    - `file_size` (required, integer) is the size, in bytes, of the file
    - `duration` (required, integer) is the duration (in total number of seconds) of the file

- `restricted_content` (very optional, array) is a list of objects that describe extended or otherwise altered versions of the same audio/video content, but restricted. For example, an ad-free or extended version of a show might be supplied for those that pay via Bitcoin. Each object in the array can contain:
    - `id` (required, string): a unique identifier for the piece of restricted content. It must be an ID not used anywhere else in the podcast, but could be a URL that resolves to a paywall page on the Web.
    - `name` (required, string): the name of the content package being offered, eg: "Premium", "Ad-free" or "Includes pre- and post-show"
    - `price` (required, positive integer): the price in satoshi for the content
    - `bitcoin_address` (required, string): the address of the Bitcoin wallet that will receive payment for the content
    - `content_audio` and/or `content_video` (at least one required, object) conforms to the `content_audio` and `content_video` specs above and describes the files the user will be able to download once payment has been confirmed.
    - `kind` (required, string): the behaviour of the content. Can be one of:
        - `primary`: this content replaces the main, unrestricted content rather than adds to it
        - `bonus`: this is bonus content that can be listened to before or after the main content
- `taxonomy_terms` (very optional, array) is a collection of taxonomy term URIs that categorise the episode. These are considered supplementary to the podcast's global taxonomy terms, so are useful for a one-off episode exploring a particular topic, or a film podcast that reviews a different film each week.

### Why no `attachments`?

The DotPodcast JSON Feed spec does not include the `attachments` array, as the podcast spec requires more information, and adding an extra `_dotpodcast` extension to each attachment object would reduce readability of the feed.

### Content URLs

It's common for podcast hosting providers to use tracking URLs in feeds, so that listener numbers can be tracked. Historically there has been no way to tie a download to a specific subscription. Part of the DotPodcast spec solves this problem via subscription tokens.

Rather than providing a direct URL to the audio/video content, or a tracking URL, podcast hosting providers must specify the URL to a thin API endpoint that exchanges a subscription token for an episode. Subscription tokens are generated when a listener subscribes to a podcast, and should be stored securely within the podcast app and in the hosting service's database. See [Requesting content](../requesting-content).

### Restricted content

Use of the term "premium" or "paid" is avoided above, but essentially this part of the spec enables content creators to charge for their work. Currently the spec does not provide an option for entire feeds to be restricted. Instead, podcasters should consider adding extra value to their free content, by providing bonus material, or content that removes advertisements.

### Why separate audio and video objects?

Some podcasts exist in both audio and video form. Podcasts that are recorded live via services like Google Hangouts or Twitch are often provided as podcasts. This enables listeners or viewers to subscribe to one podcast, but choose (at the time of subscription) in which format to receive the programme.
