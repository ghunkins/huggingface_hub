<!--⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# Cache-system reference

The caching system was updated in v0.8.0 to become the central cache-system shared
across libraries that depend on the Hub. Read the [cache-system guide](../guides/manage-cache)
for a detailed presentation of caching at HF.

## Helpers

### try_to_load_from_cache

[[autodoc]] old_huggingface_hub.try_to_load_from_cache

### cached_assets_path

[[autodoc]] old_huggingface_hub.cached_assets_path

### scan_cache_dir

[[autodoc]] old_huggingface_hub.scan_cache_dir

## Data structures

All structures are built and returned by [`scan_cache_dir`] and are immutable.

### HFCacheInfo

[[autodoc]] old_huggingface_hub.HFCacheInfo

### CachedRepoInfo

[[autodoc]] old_huggingface_hub.CachedRepoInfo
    - size_on_disk_str
    - refs

### CachedRevisionInfo

[[autodoc]] old_huggingface_hub.CachedRevisionInfo
    - size_on_disk_str
    - nb_files

### CachedFileInfo

[[autodoc]] old_huggingface_hub.CachedFileInfo
    - size_on_disk_str

### DeleteCacheStrategy

[[autodoc]] old_huggingface_hub.DeleteCacheStrategy
    - expected_freed_size_str

## Exceptions

### CorruptedCacheException

[[autodoc]] old_huggingface_hub.CorruptedCacheException
