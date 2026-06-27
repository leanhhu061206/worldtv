#!/usr/bin/env python3
"""Bootstrap per livetv.so (codice nativo compilato)."""
import importlib.util, sys
spec = importlib.util.spec_from_file_location("livetv_main", "livetvarm.so")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
mod.main()
