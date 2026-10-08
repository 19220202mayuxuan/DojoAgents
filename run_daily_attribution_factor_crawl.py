#!/usr/bin/env python3
"""Compatibility entry point for ``dojoagents attribution-factor-crawl``."""

from dojoagents.dashboard.cli.attribution_factor_crawl import (
    SectorJob,
    _build_task_command,
    main,
)

__all__ = ["SectorJob", "_build_task_command", "main"]

if __name__ == "__main__":
    raise SystemExit(main())
