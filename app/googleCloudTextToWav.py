# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.cloud import texttospeech
from google.cloud import storage

def synthesize_long_audio(project_id, location, bucketName, textToSpeak, output_file_name):
    """
    Synthesizes long input, writing the resulting audio to `output_gcs_uri`.

    Example usage: synthesize_long_audio('projectID', 'gcpLocation', 'bucketName', 'text to synthesize', 'outputFileName)

    """
    output_gcs_uri = 'gs://' + bucketName + '/' + output_file_name + '.wav'
    if(file_exists_in_gcs(bucketName, output_file_name + '.wav')):
        return
    print(output_file_name)
    client = texttospeech.TextToSpeechLongAudioSynthesizeClient()

    input = texttospeech.SynthesisInput(
        text=textToSpeak
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", name="en-US-Neural2-J"
    )

    parent = f"projects/{project_id}/locations/{location}"

    request = texttospeech.SynthesizeLongAudioRequest(
        parent=parent,
        input=input,
        audio_config=audio_config,
        voice=voice,
        output_gcs_uri=output_gcs_uri,
    )

    operation = client.synthesize_long_audio(request=request)
    # Set a deadline for your LRO to finish. 300 seconds is reasonable, but can be adjusted depending on the length of the input.
    # If the operation times out, that likely means there was an error. In that case, inspect the error, and try again.
    result = operation.result(timeout=300)
    print(
        "\nFinished processing, check your GCS bucket to find your audio file! Printing what should be an empty result: ",
        result,
    )

def file_exists_in_gcs(bucket_name, file_name):
    """
    Checks if a file exists in a Google Cloud Storage bucket.

    :param bucket_name: Name of the GCS bucket.
    :param file_name: Name of the file to check.
    :return: True if the file exists, False otherwise.
    """
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    return blob.exists()