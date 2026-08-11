# Prompt Injection Defense Example

AI agents may process external content such as documents, issues, or web data. External instructions should be treated as untrusted input.

## Recommended practices

- Separate user intent from external data.
- Validate tool calls before execution.
- Avoid exposing credentials to model context.
- Require confirmation for sensitive operations.

Nanmu treats secure agent behavior as a core design principle.