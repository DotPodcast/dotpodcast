Title: DotPodcast for directory developers
Slug: guides/directories


Podcast directories are indexes of podcasts. They are responsible for indexing and displaying podcast information.

Under the DotPodcast methodology, podcasters do not need to submit to directories. Instead, directories crawl the Blockstack `podcast` namespace for domain names, read the associated zone file and parse the JSON Feed specified in that file.

## Crawling the `podcast` namespace

More on this topic soon.

## Parsing a JSON Feed

Once you have a JSON feed to parse, read the [spec](/spec-v1) to find out what it should contain. Then find out how to [request audio/video content from the podcast](/subscription-tokens#preview-tokens).
