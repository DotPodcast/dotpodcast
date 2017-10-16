Title: Taxonomies
Slug: taxonomies


Taxonomies are groups of terms, that can be used to categorise something. For example, WordPress has two key taxonomies: Category and Tag.

Categories are hierarchical terms which should come from a fairly small list: for example: "Nature" and "Art".

Tags can be any keyword or phrase that may be used to link articles together. They don't have any relation to categories and can be pulled from a wider array of terms, like "dogs", "poker" and "painting".

Traditional podcast feeds use categories that are set out by Apple. Similarly, the DotPodcast spec has a list of categories and subcategories, but allows for more mixing and matching. For example, a music review podcast will pick one or more terms from the Music taxonomy and one or more terms from the Speech taxonomy, while a podcast that _just_ plays music may omit the Speech taxonomy terms.

Taxonomies are specified by URI rather than by name, to avoid internationalisation problems, misspellings, differences in house style ("scifi" vs "sci-fi" vs "science fiction" etc).

## Using taxonomies and terms

All taxonomies are optional, and podcasters should be able to choose one or more taxonomies, and pick from one or more terms within each taxonomy.

Taxonomies are intended to make it easier for listeners to find relevant content, not to exclude listeners or provide any kind of demographical information. The intent is to promote inclusion and open dialogue, with the ability to help listeners find voices that match their own.

## Adding taxonomies and terms

Adding and amending taxonomies and terms should be an open and democratic process. That process begins with a pull request on our [GitHub repository](https://github.com/dotpodcast/dotpodcast/), which makes the suggested changes and explains (via commit message) and suggests why these changes are necessary.

Guides on how to contribute will be released in time.

## Term nesting

Terms are hierarchical. For example "Art" is a top-level term, with "Fashion" being a sub-term. When specifying the terms applicable to a podcast, it's not necessary to specify both terms; only the lowest-level term (in this case "Fashion") needs to be selected.

However, if a podcast covers more broader topics around Art, the "Art" term can be selected, and should be considered to cover the subject broadly.

## First-party taxonomies and terms

The following are the first-party taxonomies and terms.

- [Age range](age): the suitable age range(s) for the podcast.

- [Country](country): the country or countries most relevant to the podcast (for example, a British Premier League football podcast would list "United Kingdom" as a country term).

- [Ethnicity](ethnicity): used to denote the ethnical topics discussed in the podcast (for example: a black history documentary series).

- [Format](format): the format of the podcast (live, documentary, etc).

- [Gender](gender): used to denote the gender topics discussed in the podcast (for example: a transgender panel discussion).

- [Humor](humor): the style(s) of humour employed in the podcast.

- [Language](language): the spoken language of the podcast.

- [Music](music): the genre(s) of music covered in the podcast.

- [Politics](politics): the political slant of the podcast.

- [Religion](religion): used to denote the religion(s) discussed in the podcast (for example: a Christian music review podcast).

- [Sexuality](sexuality): the sexuality or sexualities that are the focus of the podcast.

- [Subject](subject): the subject matters discussed in the podcast.

## Third-party taxonomies and terms

Although we recommend using the taxonomies laid out in this documentation, using other taxonomy URIs (as long point to pages that exist and explain the taxonomy) is perfectly fine.

One use for third-party taxonomies and terms is for TV shows, films and other pieces of pop culture. This allows deep categorisation of podcast subject matter (allowing listeners to find all the _Game of Thrones_ podcasts easily, for example) without the need for constant updates to the core spec.

A list of recognised third-party taxonomies and terms will appear below in time.
