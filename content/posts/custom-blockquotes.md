---
Title: a post with custom blockquotes
Date: 2023-05-12 15:53
Category: sample-posts
Summary: A post about custom block quotes 
Tags: 
  - formatting
  - blockquotes
related_posts: True
---

This post shows how to add custom styles for blockquotes. 

The style is similar to the custom blockquotes in [jekyll-gitbook](https://sighingnow.github.io/jekyll-gitbook/jekyll/2022-06-30-tips_warnings_dangers.html), which are also found in a lot of other sites' styles. The implementation uses the
`admonitions` extension for Python Markdown. The following
styling is found in the file `_base.scss`: 

```scss
.admonition {
  background: var(--global-bg-color);
  border-left: 5px solid var(--global-theme-color);
  margin: 1.5em 0px;
  padding: 8px;
  font-size: 1.2rem;

  p {
    margin-bottom: 0;
  }
}

.admonition.danger { 
  border-color: var(--global-danger-block);
  background-color: var(--global-danger-block-bg);

  p {
    color: var(--global-danger-block-text);
  }

  h1, h2, h3, h4, h5, h6 {
    color: var(--global-danger-block-title);
  }
}

.admonition.tip {
  border-color: var(--global-tip-block);
  background-color: var(--global-tip-block-bg);

  p {
    color: var(--global-tip-block-text);
  }

  h1, h2, h3, h4, h5, h6 {
    color: var(--global-tip-block-title);
  }
}

.admonition.warning {
  border-color: var(--global-warning-block);
  background-color: var(--global-warning-block-bg);

  p {
    color: var(--global-warning-block-text);
  }

  h1, h2, h3, h4, h5, h6 {
    color: var(--global-warning-block-title);
  }
}

.admonition-title {
  font-weight: bold;
  text-align: left;
}
```

A regular blockquote can be used as following:

```markdown
> This is a regular blockquote
> and it can be used as usual
```

> This is a regular blockquote
> and it can be used as usual

To give a tip, warning, or danger alert, try the following: 

```markdown
!!! tip
    A tip can be used when you want to give advice
    related to a certain content.
```

!!! tip
    A tip can be used when you want to give advice
    related to a certain content.

```markdown
!!! warning
    This is a warning, and thus should
    be used when you want to warn the user
```

!!! warning
    This is a warning, and thus should
    be used when you want to warn the user

```markdown
!!! danger
    This is a danger zone, and thus should
    be used carefully
```

!!! danger
    This is a danger zone, and thus should
    be used carefully