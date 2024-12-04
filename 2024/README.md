# Advent of Code

[Link to Site](https://adventofcode.com/)

## 2024

[Link to Calendar](https://adventofcode.com/2024)

#### Create a new Day from Stubs

look at [Taskfile](Taskfile.yml)

Please add a `.token` File in the folder of that year

```sh
$ touch .token
```

- then go to [AOC Login](https://adventofcode.com/2024/auth/login) and verify that you are logged in
- then go to [AOC Calendar](https://adventofcode.com/2024)
- Go to the developer tools of your browser and find the cookie `session` from the document request and copy the id

```sh
$ pbpaste > .token
```

_then you can create a new directory for a new day_

```sh
$ task create
```

#### Run the Code

```sh
$ task run -- <day>
```

For more Information look at the [readme directory of a day](./1/README.md)