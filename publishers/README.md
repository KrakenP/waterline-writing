# Publishers

Publishing is intentionally separated from writing.

## Current boundary

The writing repository may generate ready-to-publish packages, but it must not publish by default.

A platform publisher may be added only when:

1. the user wants that integration;
2. the platform offers an acceptable official or approved workflow;
3. authentication is stored outside the repository;
4. draft approval behavior is explicit;
5. the publisher can report success/failure without silently losing content.

## Interface expectation

A future publisher should accept a validated Publish Package and return a publication result such as:

```yaml
platform: wechat
status: drafted | published | failed
remote_id: string | null
remote_url: string | null
error: string | null
```

Never place API keys, cookies, OAuth tokens, or browser session data in this repository.
