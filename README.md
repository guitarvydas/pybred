# BRED - Text manipulation based on matching brackets

BRED is a tool that helps in re-formatting text.

BRED captures bits of text and allows users to fabricate new text based on the captured text.

See doc/documentation.md for further details.

# Test notes:![[README 2023-01-26 08.34.16.excalidraw]]

- parses out function names in g![[2023-01-26 08.23.53.excalidraw]]rep.c
  - repeats clear_asan_poison and ason_poison (no surprise)
```
#else
static void clear_asan_poison (void) { }
static void asan_poison (void const volatile *addr, idx_t size) { }
#endif
```
