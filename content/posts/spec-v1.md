Title: DotPodcast feed specification v1
Date: 2017-10-12
Author: Mark
Slug: spec-v1
Summary: Version 1 of the DotPodcast feed spec


The DotPodcast feed spec is inspired by the original [JSON Feed](https://jsonfeed.org/) spec, but diverges significantly in that it requires two files: a header and a body.

## The header file and the body feed

The header file is a JSON file that represents important information about the podcast. The URL to this meta file is hashed, and that hash is stored on the blockchain. The body feed contains a list of all the published episodes of the podcast.

The split is necessary because the header file does not change frequently, meaning the hash of that file also changes rarely. Changes to this kind of information take a while to propagate through the blockchain, so it would be impractical to continually push new updates to the chain upon publication of a new episode, or change to an existing episode.

## Why JSON and not RSS?

XML (on which RSS is based) is slow and difficult to parse. New apps and services built around podcasting use it because it's what everyone uses, and moving people to another system is difficult, as the RSS spec (and its podcast-specific additions, provided by Apple) were built up over time.

But since DotPodcast is making fundamental changes to the way the entire podcasting ecosystem operates, it makes sense to adopt a more easily-parsable and human-readable syntax. And so, the spec is derived from JSON Feed.

---

## [The header file](#the-header-file)

The header file contains information about the podcast itself, in JSON format. An example header file looks like this:

```json
{
    "version": "https://dotpodcast.co/spec-v1",
    "title": "My Podcast",
    "home_page_url": "https://example.com/",
    "meta_url": "https://example.com/meta.json",
    "items_url": "https://example.com/items.json",
    "subscription_url": "https://example.com/subscribe/",
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
}
```

The object contains the following:

- `version` (required, string) is the URL of the version of the format the feed uses. This is the version of the DotPodcast spec. Example: _http://dotpodcast.co/spec-v1_.

- `title` (required, string) is the name of the podcast.

- `home_page_url` (required, string) is the URL to the podcast's website.

- `meta_url` (required, string) is the URL to this header file.

- `items_url` (required, string) is the URL to the [body feed](#the-body-feed).

- `subscription_url` (required, string) is the URL to the subscription endpoint, which is used to generate a subscription token that can be exchanged when downloading episodes. See [Subscription tokens](../subscription-tokens) for more information.

- `author` (optional, object) specifies the podcast author. The author object has several members. These are all optional, but if you provide an author object, then at least one is required:

  - `name` (optional, string) is the author’s name.

  - `url` (optional, string) is the URL of a site owned by the author. It could be a blog, microblog, Twitter account, and so on. Ideally the linked-to page provides a way to contact the author, but that’s not required.

  - `avatar` (optional, string) is the URL for an image for the author. It should be square and relatively large — such as 512x512 — and should use transparency where appropriate, since it may be rendered on a non-white background.

- `artwork` (optional but highly recommended, object) specifies the podcast cover artwork at varying sizes:
    - `@1x` (required, string) is the URL to a 1400x1400 image.
    - `@2x` (required, string) is the URL to a 2800x2800 image.
    - Any other sizes can be added here, that may be supported by third-party directories such as Apple Podcasts.

- `expired` (optional, boolean) says whether or not the podcast is finished (that is, whether or not it will ever update again). If the value is `true`, then it’s expired. Any other value, or the absence of `expired`, means the feed may continue to update.

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

## [The body feed](#the-body-feed)

The body feed is a JSON-formatted array of episodes. An example feed looks like this:

```json
{
    "meta": {
        "version": "https://dotpodcast.co/spec-v1",
        "next_url": "https://example.com/items.json?page=2",
        "previous_url": null,
        "total_count": 30,
        "per_page": 10
    },
    "items": [
        {
            "id": "1",
            "title": "Episode one",
            "url": "https://example.com/1/",
            "content_audio": {
                "mime_type": "audio/mpeg",
                "url": "https://example.com/1/download/",
                "file_size": 28800000
            },
            "content_text": "This is the first episode.",
        },
        ...
    ]
}
```

### The `meta` object

The `meta` object contains information about the returned data, and a simple way to retrieve the next set of items.

The `version` property is required, and should be the URL of the version of the format the feed uses. It should be the same as that specified in the header file.

The hosting provider may choose to paginate results, delivering, say, 10 results per page. In this case, the `next_url` property should contain a full URL to the next set of 10 results. If the second page of results is being returned, `previous_url` should point to the previous page.

`total_count` should return the total number of episodes available in the feed, and `per_page` should return the number of episodes in this current paginated list.

### The `items` object

This should be an array of published episodes. An item object contains:

- `id` (required, string) is unique for that episode. If an episode is ever updated, the ID should be unchanged. New episodes should never use a previously-used ID. If an ID is presented as a number or other type, a podcast app or directory service must coerce it to a string. Ideally, the ID is the full URL of the episode's web page (not the episode audio or video content), since URLs make great unique identifiers.

- `url` (optional, string) is the URL of the episode. It’s the permalink. This may be the same as the ID, but should be present regardless.

- `title` (optional, string) is the plain text episode title.

- `summary` (optional, string) is a plain text sentence or two describing the episode.

- `season_number` (optional, integer) is the season number of the podcast, if applicable. If not, the value should be omitted.

- `episode_number` (optional, integer) is the number of the episode within the season. If the podcast is not season-based, this value, along with `season_number` should be omitted.

- `subtitle` (optional, string) is a short sentence that describes the episode.

- `content_html` and `content_text` are each optional strings, but one or both must be present. This is the HTML or plain text of the item. Important: the only place HTML is allowed in this format is in `content_html`.

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

### Content URLs

It's common for podcast hosting providers to use tracking URLs in feeds, so that listener numbers can be tracked. Historically there has been no way to tie a download to a specific subscription. Part of the DotPodcast spec solves this problem via subscription tokens.

Rather than providing a direct URL to the audio/video content, or a tracking URL, podcast hosting providers must specify the URL to a thin API endpoint that exchanges a subscription token for an episode. Subscription tokens are generated when a listener subscribes to a podcast, and should be stored securely within the podcast app and in the hosting service's database. See [Requesting content](../requesting-content).

### Restricted content

Use of the term "premium" or "paid" is avoided above, but essentially this part of the spec enables content creators to charge for their work. Currently the spec does not provide an option for entire feeds to be restricted. Instead, podcasters should consider adding extra value to their free content, by providing bonus material, or content that removes advertisements.

### Why separate audio and video objects?

Some podcasts exist in both audio and video form. Podcasts that are recorded live via services like Google Hangouts or Twitch are often provided as podcasts. This enables listeners or viewers to subscribe to one podcast, but choose (at the time of subscription) in which format to receive the programme.
