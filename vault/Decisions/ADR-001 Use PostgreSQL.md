---
type: adr
status: accepted
date: 2026-01-15
deciders: [team]
tags: [adr, database]
---
# ADR-001: Use PostgreSQL as the primary database

## Context
We need relational data, transactions and JSON fields for a small web app.

## Decision
Use PostgreSQL for all persistent application data.

## Consequences
- One well-known database to operate and back up.
- JSON columns cover semi-structured data without a second store.

Related: [[Decisions Index]]
