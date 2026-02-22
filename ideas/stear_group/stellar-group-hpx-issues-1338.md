# Here

**Parent:** Ste||ar group — Project Ideas
**Source:** https://github.com/STEllAR-GROUP/hpx/issues/1338
**Scraped:** 2026-02-22T23:28:47.614375

---

## Extend parallel algorithms to work with hpx::partitioned_vector et.al.

**Labels:** type: enhancement, category: algorithms, category: data-structures, tag: pinned

The existing parallel algorithms should be extended to seamlessly work with distributed data structures like `hpx::partitioned_vector`. Unfortunately this requires additional code for each specific algorithms.

For more information about the parallel algorithms already implemented see #1141.

Here is the list of algorithms mandated by N4310 which should be ported to the distributed case:
- [x] `adjacent_difference` (see #2859, #3525)
- [x] `adjacent_find` (see #2859, #3525)
- [x] `all_of` `any_of` `none_of` (see #2859, #3525)
- [x] `copy` (see #1346) `copy_n` 
- [ ] `copy_if` 
- [x] `move` (see #2010)
- [x] `count` `count_if` (see #1340)
- [ ] `equal` `mismatch`
- [x] `exclusive_scan` `inclusive_scan` (see #2287)
- [x] `reduce` `transform`  (see #2725)
- [x] `fill` (#2202)
- [ ] `fill_n`
- [x] `find` `find_if` `find_if_not` (see #2792) 
- [ ] `find_end` `find_first_of` (see #2793)
- [x] `for_each` 
- [x] `for_each_n` (see #2725)
- [x] `generate` (see #1968) 
- [ ] `generate_n`
- [ ] `inner_product` `inplace_merge` `merge`
- [ ] `is_heap` `is_heap_until`
- [ ] `is_partitioned` `is_sorted` `is_sorted_until`
- [ ] `lexicographical_compare`
- [x] `max_element` `min_element` `minmax_element` (#1968)
- [ ] `partial_sort` `partial_sort_copy` `partition` `partition_copy` `nth_element` `sort` `stable_partition` `stable_sort`
- [ ] `remove` `remove_copy` `remove_copy_if` `remove_if`
- [ ] `replace` `replace_copy` `replace_copy_if` `replace_if` 
- [ ] `reverse` `reverse_copy` 
- [ ] `rotate` `rotate_copy`
- [ ] `search` `search_n` 
- [ ] `set_difference` `set_intersection` `set_symmetric_difference` `set_union` `includes`
- [ ] `swap_ranges`
- [ ] `uninitialized_copy` `uninitialized_copy_n`
- [ ] `uninitialized_fill` `uninitialized_fill_n`
- [ ] `unique` `unique_copy`

These were added by N4310:
- [x] `transform_reduce` (see #1333, #2859, #3525)
- [x] `transform_exclusive_scan` `transform_inclusive_scan`  (see #2725)

