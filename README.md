# BRED - Text manipulation based on matching brackets
![bred](./doc/bred.png)

BRED is a tool that helps in re-formatting text.

BRED captures bits of text and allows users to fabricate new text based on the captured text.

See doc/documentation.md for further details.

# Test notes:

- parses out function names in grep.c
  - repeats clear_asan_poison and ason_poison (no surprise)
```
#else
static void clear_asan_poison (void) { }
static void asan_poison (void const volatile *addr, idx_t size) { }
#endif
```
