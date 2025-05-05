<!--⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# HfApi Client[[hfapi-client]]

아래는 허깅 페이스 Hub의 API를 위한 파이썬 래퍼인 `HfApi` 클래스에 대한 문서입니다.

`HfApi`의 모든 메서드는 패키지의 루트에서 직접 접근할 수 있습니다. 두 접근 방식은 아래에서 자세히 설명합니다.

루트 메서드를 사용하는 것이 더 간단하지만 [`HfApi`] 클래스를 사용하면 더 유연하게 사용할 수 있습니다.
특히 모든 HTTP 호출에서 재사용할 토큰을 전달할 수 있습니다. 
이 방식은 토큰이 머신에 유지되지 않기 때문에 `huggingface-cli login` 또는 [`login`]를 사용하는 방식과는 다르며,
다른 엔드포인트를 제공하거나 사용자정의 에이전트를 구성할 수도 있습니다.

```python
from old_huggingface_hub import HfApi, list_models

# 루트 메서드를 사용하세요.
models = list_models()

# 또는 HfApi client를 구성하세요.
hf_api = HfApi(
    endpoint="https://huggingface.co", # 비공개 Hub 엔드포인트를 지정할 수 있습니다.
    token="hf_xxx", # 토큰은 머신에 유지되지 않습니다.
)
models = hf_api.list_models()
```

## HfApi[[old_huggingface_hub.HfApi]]

[[autodoc]] HfApi

[[autodoc]] plan_multi_commits

## API Dataclasses[[api-dataclasses]]

### AccessRequest[[old_huggingface_hub.hf_api.AccessRequest]]

[[autodoc]] old_huggingface_hub.hf_api.AccessRequest

### CommitInfo[[old_huggingface_hub.CommitInfo]]

[[autodoc]] old_huggingface_hub.hf_api.CommitInfo

### DatasetInfo[[old_huggingface_hub.hf_api.DatasetInfo]]

[[autodoc]] old_huggingface_hub.hf_api.DatasetInfo

### GitRefInfo[[old_huggingface_hub.GitRefInfo]]

[[autodoc]] old_huggingface_hub.hf_api.GitRefInfo

### GitCommitInfo[[old_huggingface_hub.GitCommitInfo]]

[[autodoc]] old_huggingface_hub.hf_api.GitCommitInfo

### GitRefs[[old_huggingface_hub.GitRefs]]

[[autodoc]] old_huggingface_hub.hf_api.GitRefs

### ModelInfo[[old_huggingface_hub.hf_api.ModelInfo]]

[[autodoc]] old_huggingface_hub.hf_api.ModelInfo

### RepoSibling[[old_huggingface_hub.hf_api.RepoSibling]]

[[autodoc]] old_huggingface_hub.hf_api.RepoSibling

### RepoFile[[old_huggingface_hub.hf_api.RepoFile]]

[[autodoc]] old_huggingface_hub.hf_api.RepoFile

### RepoUrl[[old_huggingface_hub.RepoUrl]]

[[autodoc]] old_huggingface_hub.hf_api.RepoUrl

### SafetensorsRepoMetadata[[old_huggingface_hub.utils.SafetensorsRepoMetadata]]

[[autodoc]] old_huggingface_hub.utils.SafetensorsRepoMetadata

### SafetensorsFileMetadata[[old_huggingface_hub.utils.SafetensorsFileMetadata]]

[[autodoc]] old_huggingface_hub.utils.SafetensorsFileMetadata

### SpaceInfo[[old_huggingface_hub.hf_api.SpaceInfo]]

[[autodoc]] old_huggingface_hub.hf_api.SpaceInfo

### TensorInfo[[old_huggingface_hub.utils.TensorInfo]]

[[autodoc]] old_huggingface_hub.utils.TensorInfo

### User[[old_huggingface_hub.User]]

[[autodoc]] old_huggingface_hub.hf_api.User

### UserLikes[[old_huggingface_hub.UserLikes]]

[[autodoc]] old_huggingface_hub.hf_api.UserLikes

## CommitOperation[[old_huggingface_hub.CommitOperationAdd]]

[`CommitOperation`]에 지원되는 값은 다음과 같습니다:

[[autodoc]] CommitOperationAdd

[[autodoc]] CommitOperationDelete

[[autodoc]] CommitOperationCopy

## CommitScheduler[[old_huggingface_hub.CommitScheduler]]

[[autodoc]] CommitScheduler

## Search helpers[[search-helpers]]

`old_huggingface_hub` 패키지에는 Hub에서 리포지토리를 필터링하는 데 도움되는 도구들이 포함되어 있습니다.

### DatasetFilter[[old_huggingface_hub.DatasetFilter]]

[[autodoc]] DatasetFilter

### ModelFilter[[old_huggingface_hub.ModelFilter]]

[[autodoc]] ModelFilter
