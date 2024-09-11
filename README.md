# Static Site Generator

## Overview

This program generates a static website from Markdown files.

Example content and styling can be found in the `content` and `static` directories, respectively.

## Usage

To run the program, run the shell script `./main.sh`

Add your own content to the `content` directory and use the `static` directory to add images, styling and other files.

Once you have added your Markdown content, run the shell script again. It will generate the static website in the `public` directory.

Your content must be valid Markdown. The basic Markdown syntax is supported:

Heading - `# H1 text` - `## H2 text` - `### H3 text`

Bold - `**bold text**`

Italic - `*italic text*`

Code - `` `code text` ``

Link -`[text](url)`Image -`![alt text](url)`

Unordered list -`- item 1 text`-`- item 2 text`

Ordered list -`1. item 1 text`-`2. item 2 text`
