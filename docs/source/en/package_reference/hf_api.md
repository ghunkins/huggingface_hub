<!--⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# HfApi Client

Below is the documentation for the `HfApi` class, which serves as a Python wrapper for the Hugging Face Hub's API.

All methods from the `HfApi` are also accessible from the package's root directly. Both approaches are detailed below.

Using the root method is more straightforward but the [`HfApi`] class gives you more flexibility.
In particular, you can pass a token that will be reused in all HTTP calls. This is different
than `huggingface-cli login` or [`login`] as the token is not persisted on the machine.
It is also possible to provide a different endpoint or configure a custom user-agent.

```python
from old_huggingface_hub import HfApi, list_models

# Use root method
models = list_models()

# Or configure a HfApi client
hf_api = HfApi(
    endpoint="https://huggingface.co", # Can be a Private Hub endpoint.
    token="hf_xxx", # Token is not persisted on the machine.
)
models = hf_api.list_models()
```

## HfApi

[[autodoc]] HfApi

[[autodoc]] plan_multi_commits

## API Dataclasses

### AccessRequest

[[autodoc]] old_huggingface_hub.hf_api.AccessRequest

### CommitInfo

[[autodoc]] old_huggingface_hub.hf_api.CommitInfo

### DatasetInfo

[[autodoc]] old_huggingface_hub.hf_api.DatasetInfo

### GitRefInfo

[[autodoc]] old_huggingface_hub.hf_api.GitRefInfo

### GitCommitInfo

[[autodoc]] old_huggingface_hub.hf_api.GitCommitInfo

### GitRefs

[[autodoc]] old_huggingface_hub.hf_api.GitRefs

### ModelInfo

[[autodoc]] old_huggingface_hub.hf_api.ModelInfo

### RepoSibling

[[autodoc]] old_huggingface_hub.hf_api.RepoSibling

### RepoFile

[[autodoc]] old_huggingface_hub.hf_api.RepoFile

### RepoUrl

[[autodoc]] old_huggingface_hub.hf_api.RepoUrl

### SafetensorsRepoMetadata

[[autodoc]] old_huggingface_hub.utils.SafetensorsRepoMetadata

### SafetensorsFileMetadata

[[autodoc]] old_huggingface_hub.utils.SafetensorsFileMetadata

### SpaceInfo

[[autodoc]] old_huggingface_hub.hf_api.SpaceInfo

### TensorInfo

[[autodoc]] old_huggingface_hub.utils.TensorInfo

### User

[[autodoc]] old_huggingface_hub.hf_api.User

### UserLikes

[[autodoc]] old_huggingface_hub.hf_api.UserLikes

## CommitOperation

Below are the supported values for [`CommitOperation`]:

[[autodoc]] CommitOperationAdd

[[autodoc]] CommitOperationDelete

[[autodoc]] CommitOperationCopy

## CommitScheduler

[[autodoc]] CommitScheduler

## Search helpers

Some helpers to filter repositories on the Hub are available in the `old_huggingface_hub` package.

### DatasetFilter

[[autodoc]] DatasetFilter

### ModelFilter

[[autodoc]] ModelFilter
