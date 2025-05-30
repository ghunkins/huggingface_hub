
<!--⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->
<!--⚠️ Note that this file is auto-generated by `utils/generate_inference_types.py`. Do not modify it manually.-->


# Inference types

This page lists the types (e.g. dataclasses) available for each task supported on the Hugging Face Hub.
Each task is specified using a JSON schema, and the types are generated from these schemas - with some customization
due to Python requirements.
Visit [@huggingface.js/tasks](https://github.com/huggingface/huggingface.js/tree/main/packages/tasks/src/tasks)
to find the JSON schemas for each task.

This part of the lib is still under development and will be improved in future releases.



## audio_classification

[[autodoc]] old_huggingface_hub.AudioClassificationInput

[[autodoc]] old_huggingface_hub.AudioClassificationOutputElement

[[autodoc]] old_huggingface_hub.AudioClassificationParameters



## audio_to_audio

[[autodoc]] old_huggingface_hub.AudioToAudioInput

[[autodoc]] old_huggingface_hub.AudioToAudioOutputElement



## automatic_speech_recognition

[[autodoc]] old_huggingface_hub.AutomaticSpeechRecognitionGenerationParameters

[[autodoc]] old_huggingface_hub.AutomaticSpeechRecognitionInput

[[autodoc]] old_huggingface_hub.AutomaticSpeechRecognitionOutput

[[autodoc]] old_huggingface_hub.AutomaticSpeechRecognitionOutputChunk

[[autodoc]] old_huggingface_hub.AutomaticSpeechRecognitionParameters



## chat_completion

[[autodoc]] old_huggingface_hub.ChatCompletionInput

[[autodoc]] old_huggingface_hub.ChatCompletionInputFunctionDefinition

[[autodoc]] old_huggingface_hub.ChatCompletionInputMessage

[[autodoc]] old_huggingface_hub.ChatCompletionInputTool

[[autodoc]] old_huggingface_hub.ChatCompletionInputToolCall

[[autodoc]] old_huggingface_hub.ChatCompletionInputToolTypeClass

[[autodoc]] old_huggingface_hub.ChatCompletionOutput

[[autodoc]] old_huggingface_hub.ChatCompletionOutputComplete

[[autodoc]] old_huggingface_hub.ChatCompletionOutputFunctionDefinition

[[autodoc]] old_huggingface_hub.ChatCompletionOutputLogprob

[[autodoc]] old_huggingface_hub.ChatCompletionOutputLogprobs

[[autodoc]] old_huggingface_hub.ChatCompletionOutputMessage

[[autodoc]] old_huggingface_hub.ChatCompletionOutputToolCall

[[autodoc]] old_huggingface_hub.ChatCompletionOutputTopLogprob

[[autodoc]] old_huggingface_hub.ChatCompletionOutputUsage

[[autodoc]] old_huggingface_hub.ChatCompletionStreamOutput

[[autodoc]] old_huggingface_hub.ChatCompletionStreamOutputChoice

[[autodoc]] old_huggingface_hub.ChatCompletionStreamOutputDelta

[[autodoc]] old_huggingface_hub.ChatCompletionStreamOutputDeltaToolCall

[[autodoc]] old_huggingface_hub.ChatCompletionStreamOutputFunction

[[autodoc]] old_huggingface_hub.ChatCompletionStreamOutputLogprob

[[autodoc]] old_huggingface_hub.ChatCompletionStreamOutputLogprobs

[[autodoc]] old_huggingface_hub.ChatCompletionStreamOutputTopLogprob



## depth_estimation

[[autodoc]] old_huggingface_hub.DepthEstimationInput

[[autodoc]] old_huggingface_hub.DepthEstimationOutput



## document_question_answering

[[autodoc]] old_huggingface_hub.DocumentQuestionAnsweringInput

[[autodoc]] old_huggingface_hub.DocumentQuestionAnsweringInputData

[[autodoc]] old_huggingface_hub.DocumentQuestionAnsweringOutputElement

[[autodoc]] old_huggingface_hub.DocumentQuestionAnsweringParameters



## feature_extraction

[[autodoc]] old_huggingface_hub.FeatureExtractionInput



## fill_mask

[[autodoc]] old_huggingface_hub.FillMaskInput

[[autodoc]] old_huggingface_hub.FillMaskOutputElement

[[autodoc]] old_huggingface_hub.FillMaskParameters



## image_classification

[[autodoc]] old_huggingface_hub.ImageClassificationInput

[[autodoc]] old_huggingface_hub.ImageClassificationOutputElement

[[autodoc]] old_huggingface_hub.ImageClassificationParameters



## image_segmentation

[[autodoc]] old_huggingface_hub.ImageSegmentationInput

[[autodoc]] old_huggingface_hub.ImageSegmentationOutputElement

[[autodoc]] old_huggingface_hub.ImageSegmentationParameters



## image_to_image

[[autodoc]] old_huggingface_hub.ImageToImageInput

[[autodoc]] old_huggingface_hub.ImageToImageOutput

[[autodoc]] old_huggingface_hub.ImageToImageParameters

[[autodoc]] old_huggingface_hub.ImageToImageTargetSize



## image_to_text

[[autodoc]] old_huggingface_hub.ImageToTextGenerationParameters

[[autodoc]] old_huggingface_hub.ImageToTextInput

[[autodoc]] old_huggingface_hub.ImageToTextOutput

[[autodoc]] old_huggingface_hub.ImageToTextParameters



## object_detection

[[autodoc]] old_huggingface_hub.ObjectDetectionBoundingBox

[[autodoc]] old_huggingface_hub.ObjectDetectionInput

[[autodoc]] old_huggingface_hub.ObjectDetectionOutputElement

[[autodoc]] old_huggingface_hub.ObjectDetectionParameters



## question_answering

[[autodoc]] old_huggingface_hub.QuestionAnsweringInput

[[autodoc]] old_huggingface_hub.QuestionAnsweringInputData

[[autodoc]] old_huggingface_hub.QuestionAnsweringOutputElement

[[autodoc]] old_huggingface_hub.QuestionAnsweringParameters



## sentence_similarity

[[autodoc]] old_huggingface_hub.SentenceSimilarityInput

[[autodoc]] old_huggingface_hub.SentenceSimilarityInputData



## summarization

[[autodoc]] old_huggingface_hub.SummarizationGenerationParameters

[[autodoc]] old_huggingface_hub.SummarizationInput

[[autodoc]] old_huggingface_hub.SummarizationOutput



## table_question_answering

[[autodoc]] old_huggingface_hub.TableQuestionAnsweringInput

[[autodoc]] old_huggingface_hub.TableQuestionAnsweringInputData

[[autodoc]] old_huggingface_hub.TableQuestionAnsweringOutputElement



## text2text_generation

[[autodoc]] old_huggingface_hub.Text2TextGenerationInput

[[autodoc]] old_huggingface_hub.Text2TextGenerationOutput

[[autodoc]] old_huggingface_hub.Text2TextGenerationParameters



## text_classification

[[autodoc]] old_huggingface_hub.TextClassificationInput

[[autodoc]] old_huggingface_hub.TextClassificationOutputElement

[[autodoc]] old_huggingface_hub.TextClassificationParameters



## text_generation

[[autodoc]] old_huggingface_hub.TextGenerationInput

[[autodoc]] old_huggingface_hub.TextGenerationInputGenerateParameters

[[autodoc]] old_huggingface_hub.TextGenerationInputGrammarType

[[autodoc]] old_huggingface_hub.TextGenerationOutput

[[autodoc]] old_huggingface_hub.TextGenerationOutputBestOfSequence

[[autodoc]] old_huggingface_hub.TextGenerationOutputDetails

[[autodoc]] old_huggingface_hub.TextGenerationOutputPrefillToken

[[autodoc]] old_huggingface_hub.TextGenerationOutputToken

[[autodoc]] old_huggingface_hub.TextGenerationStreamOutput

[[autodoc]] old_huggingface_hub.TextGenerationStreamOutputStreamDetails

[[autodoc]] old_huggingface_hub.TextGenerationStreamOutputToken



## text_to_audio

[[autodoc]] old_huggingface_hub.TextToAudioGenerationParameters

[[autodoc]] old_huggingface_hub.TextToAudioInput

[[autodoc]] old_huggingface_hub.TextToAudioOutput

[[autodoc]] old_huggingface_hub.TextToAudioParameters



## text_to_image

[[autodoc]] old_huggingface_hub.TextToImageInput

[[autodoc]] old_huggingface_hub.TextToImageOutput

[[autodoc]] old_huggingface_hub.TextToImageParameters

[[autodoc]] old_huggingface_hub.TextToImageTargetSize



## token_classification

[[autodoc]] old_huggingface_hub.TokenClassificationInput

[[autodoc]] old_huggingface_hub.TokenClassificationOutputElement

[[autodoc]] old_huggingface_hub.TokenClassificationParameters



## translation

[[autodoc]] old_huggingface_hub.TranslationGenerationParameters

[[autodoc]] old_huggingface_hub.TranslationInput

[[autodoc]] old_huggingface_hub.TranslationOutput



## video_classification

[[autodoc]] old_huggingface_hub.VideoClassificationInput

[[autodoc]] old_huggingface_hub.VideoClassificationOutputElement

[[autodoc]] old_huggingface_hub.VideoClassificationParameters



## visual_question_answering

[[autodoc]] old_huggingface_hub.VisualQuestionAnsweringInput

[[autodoc]] old_huggingface_hub.VisualQuestionAnsweringInputData

[[autodoc]] old_huggingface_hub.VisualQuestionAnsweringOutputElement

[[autodoc]] old_huggingface_hub.VisualQuestionAnsweringParameters



## zero_shot_classification

[[autodoc]] old_huggingface_hub.ZeroShotClassificationInput

[[autodoc]] old_huggingface_hub.ZeroShotClassificationInputData

[[autodoc]] old_huggingface_hub.ZeroShotClassificationOutputElement

[[autodoc]] old_huggingface_hub.ZeroShotClassificationParameters



## zero_shot_image_classification

[[autodoc]] old_huggingface_hub.ZeroShotImageClassificationInput

[[autodoc]] old_huggingface_hub.ZeroShotImageClassificationInputData

[[autodoc]] old_huggingface_hub.ZeroShotImageClassificationOutputElement

[[autodoc]] old_huggingface_hub.ZeroShotImageClassificationParameters



## zero_shot_object_detection

[[autodoc]] old_huggingface_hub.ZeroShotObjectDetectionBoundingBox

[[autodoc]] old_huggingface_hub.ZeroShotObjectDetectionInput

[[autodoc]] old_huggingface_hub.ZeroShotObjectDetectionInputData

[[autodoc]] old_huggingface_hub.ZeroShotObjectDetectionOutputElement


