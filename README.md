# Weat_project

## Description
What you should learn from this project:

* How to read API documentation to find the endpoints you’re looking for
* How to use an API with pagination
* How to parse JSON results from an API
* How to make a recursive API call
* How to sort a dictionary by value

---

## Tasks

### [0. How many subs?](./0-subs.py)

- Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
- Requirements:

  - Prototype: `def number_of_subscribers(subreddit)`
  - If not a valid subreddit, return 0.
  - NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

```sh
wintermancer@lapbox ~/reddit_api/project $ cat 0-main.py
```

```python
#!/usr/bin/python3
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
```

```sh
wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py programming
756024
wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py this_is_a_fake_subreddit
0
```





---

## Author
* **Van Phan** - [vdphan](https://github.com/vdphan) [mail](duyphan0@gmail.com)
