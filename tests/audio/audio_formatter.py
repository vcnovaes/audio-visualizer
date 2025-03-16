import pytest
from unittest.mock import patch, MagicMock
from src.audio.audio_formatter import AudioFormatter
from src.patterns.result import Result


def test_is_wav():
    assert AudioFormatter._AudioFormatter__is_wav("test.wav") is True
    assert AudioFormatter._AudioFormatter__is_wav("test.mp3") is False
    assert AudioFormatter._AudioFormatter__is_wav("test.txt") is False


def test_get_format():
    assert AudioFormatter._AudioFormatter__get_format("test.wav") == "wav"
    assert AudioFormatter._AudioFormatter__get_format("test.mp3") == "mp3"
    assert AudioFormatter._AudioFormatter__get_format("test.txt") == "txt"


def test_validate_format_supported():
    result = AudioFormatter._AudioFormatter__validate_format("test.wav")
    assert result.is_ok()
    assert result.unwrap()[0] == "wav"

    result = AudioFormatter._AudioFormatter__validate_format("test.mp3")
    assert result.is_ok()
    assert result.unwrap()[0] == "mp3"


def test_validate_format_unsupported():
    result = AudioFormatter._AudioFormatter__validate_format("test.txt")
    assert not result.is_ok()
    assert result.unwrap()[1] == "Unsupported format: txt"


@patch("src.audio.audio_formatter.AudioSegment.from_file")
@patch("src.audio.audio_formatter.AudioSegment.export")
def test_convert_to_wav_success(mock_export, mock_from_file):
    mock_audio = MagicMock()
    mock_from_file.return_value = mock_audio
    mock_export.return_value = None

    result = AudioFormatter.convert_to_wav("test.mp3", "output.wav")
    assert result.is_ok()
    assert result.unwrap()[0] == "output.wav"

    mock_from_file.assert_called_once_with("test.mp3", format="mp3")
    mock_audio.export.assert_called_once_with("output.wav", format="wav")


def test_convert_to_wav_already_wav():
    result = AudioFormatter.convert_to_wav("test.wav", "output.wav")
    assert result.is_ok()
    assert result.unwrap()[0] == "output.wav"


def test_convert_to_wav_unsupported_format():
    result = AudioFormatter.convert_to_wav("test.txt", "output.wav")
    assert not result.is_ok()
    assert result.unwrap()[1] == "Unsupported format: txt"
