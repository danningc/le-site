---
title: MCP Tools & Cloud Automation
type: concept
public: false
tags: [ai, mcp, automation, gmail, claude-code, scheduling]
updated: 2026-05-08
---

# MCP Tools & Cloud Automation

MCP (Model Context Protocol) is how Claude Code connects to external services — Gmail, Google Calendar, Google Drive, and others. Instead of writing code to call APIs yourself, you talk to Claude and it calls the tools on your behalf.

## What MCP Enables

MCP connectors expose real-world services as tools Claude can call mid-conversation:

| Connector | What it can do |
|-----------|---------------|
| **Gmail** | Search emails, read threads, send, draft, label, mark read/unread |
| **Google Calendar** | List, create, update, delete events; suggest times |
| **Google Drive** | Search, read, create, copy files |

Connectors are configured at [claude.ai/customize/connectors](https://claude.ai/customize/connectors) and are available both in interactive sessions and in cloud-scheduled routines.

## Gmail MCP — Key Patterns

**Searching emails:**
Use `search_emails` with Gmail query syntax — `is:unread`, `from:someone@example.com`, `subject:keyword`, etc.

**Reading an email:**
`read_email` by message ID — returns full thread content.

**Marking as read:**
`modify_email` to remove the `UNREAD` label. This is how Gmail works under the hood — "read" just means the UNREAD label is absent.

**Sending an email:**
`send_email` with `to`, `subject`, `body`. The sender is the connected Gmail account.

## Cloud Routines (RemoteTrigger)

A cloud routine is a scheduled Claude agent that runs in Anthropic's infrastructure — not locally. It survives after you close your session.

**Anatomy of a routine:**
- **Name** — human label
- **Cron expression** — when to run (UTC, minimum 1-hour interval)
- **Prompt** — the self-contained instructions for the remote agent (it starts with zero context)
- **MCP connections** — which connectors to attach (Gmail, etc.)
- **Environment** — where it runs (Anthropic cloud)

**Important:** The remote agent has no access to local files, local environment variables, or your machine. The prompt must be fully self-contained.

**Timezone gotcha:** Cron expressions are in UTC. `0 6 * * *` = 8am Amsterdam CEST (UTC+2). Always confirm the conversion before saving.

## The /loop and /schedule Skills

- `/loop <prompt>` — runs a task repeatedly in your current session. For daily cadence, it offers to upgrade to a cloud schedule.
- `/schedule` — creates a RemoteTrigger routine directly. Used when you want something to keep running after session close.

## Email Triage Pattern

A useful automation: each morning, a cloud routine checks unread emails, summarizes them, and emails you a digest with suggested actions. You reply to the digest to indicate what needs follow-up. This keeps Claude as the first filter — you only see what matters.

**Routine configuration used:**
- Cron: `0 6 * * *` (8am Amsterdam)
- MCP: Gmail
- Prompt: search unread → read each → send summary to user email with sender/subject/1-line summary/suggested action → ask user to reply with instructions

## Managing Routines

- View and manage: [claude.ai/code/routines](https://claude.ai/code/routines)
- To delete a routine: use the web UI (API deletion not supported via CLI)
- To re-arm a one-shot routine: update it with a new `run_once_at` timestamp

## Related

- [[AI Agents]] — broader concept of agents, tools, and automation
- [[5-Day AI Agent Course]] — hands-on course where agent-building was explored
