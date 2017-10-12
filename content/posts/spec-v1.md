Title: DotPodcast JSON feed specification v1
Date: 2017-10-12
Author: Mark
Summary: Version 1 of the DotPodcast JSON Feed spec


The DotPodcast JSON Feed spec is derived from the original
[JSON Feed](https://jsonfeed.org/) spec, and makes no modifications
to its structure. A sample, taken directly from their documentation
looks like this:

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

XML (on which RSS is based) is slow and difficult to parse. New apps
and services built around podcasting use it because it's what everyone
uses, and moving people to another system is difficult, as the RSS spec
(and its podcast-specific additions, provided by Apple) were built up
over time.

But since DotPodcast is making fundamental changes to the way the
entire podcasting ecosystem operates, it makes sense to adopt a more
easily-parsable and human-readable syntax. And so, JSON Feed.

### Our JSON Feed extension

Our spec adds an extension called `_podcast` to the header section
(before the `items` list) and the `items` list itself. For example:

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

The header `_dotpodcast` object is the one that appears before the
list of items. It contains information about the podcast itself, that
isn't covered by the JSON Feed spec.
