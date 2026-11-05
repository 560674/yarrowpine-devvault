---
type: snippet
language: python
tags: [snippet, python, reliability]
---
# Retry with exponential backoff

```python
import random, time

def retry(fn, attempts=5, base=0.5):
    for i in range(attempts):
        try:
            return fn()
        except Exception:
            if i == attempts - 1:
                raise
            time.sleep(base * 2 ** i + random.random() * base)
```

**Gotchas:** only retry idempotent operations.

Back to [[Snippets Index]]
