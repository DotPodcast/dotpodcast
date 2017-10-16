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

### Why JSON and not RSS?

XML (on which RSS is based) is slow and difficult to parse. New apps and services built around podcasting use it because it's what everyone uses, and moving people to another system is difficult, as the RSS spec (and its podcast-specific additions, provided by Apple) were built up over time.

But since DotPodcast is making fundamental changes to the way the entire podcasting ecosystem operates, it makes sense to adopt a more easily-parsable and human-readable syntax. And so, JSON Feed.

### Our JSON Feed extension

Our spec adds an extension called `_dotpodcast` to the header section (before the `items` list) and the `items` list itself. For example:

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

### The header object

The header `_dotpodcast` object is the one that appears before the list of items. It contains information about the podcast itself, that isn't covered by the JSON Feed spec.

- `version` (required, string) is the URL of the version of the format the feed uses. This is the version of the DotPodcast spec, not the
JSON Feed format. Example: _http://dotpodcast.org/spec-v1_.

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

### Why no language tag?

The spoken language used in the podcast should be added as a taxonomy term, as it may not always be relevant ( music podcasts with no presenters may have no spoken language, and some podcasts may even use multiple languages).

### Why no "explicit" tag?

Instead of marking a show as containing "explicit" language or not, podcasters are encouraged to use a taxonomy term that denotes the level of profanity being used.

---

### The
