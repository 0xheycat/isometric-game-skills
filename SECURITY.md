# Security Policy

## Scope

This repository is a collection of **documentation skills, example code, and small
utility scripts** for building isometric games. It ships no servers, no network
services, and no production runtime. The realistic security surface is limited to:

- The example/demo code (`demo/`, `engine/`, `examples/`).
- The helper scripts (`scripts/`, ComfyUI workflow builders).
- The CI workflow (`.github/workflows/`).

## Reporting a Vulnerability

If you find a security issue — for example, a script that could execute untrusted
input, or a CI misconfiguration — please report it privately:

1. Open a **GitHub Security Advisory** via the repository's **Security → Report a
   vulnerability** tab (preferred), **or**
2. Open a regular issue **without sensitive details** asking a maintainer to make
   contact.

Please do **not** open a public issue containing exploit details until a fix is
available.

## Response

This is a community project maintained on a best-effort basis. We aim to
acknowledge valid reports within **7 days** and to address confirmed issues in a
timely follow-up release.

## Good to know

- Never commit model weights, API keys, or `.env` files — see [`.gitignore`](.gitignore).
- The demo and engine run entirely client-side / locally; nothing is sent
  anywhere.
