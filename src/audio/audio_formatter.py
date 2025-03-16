from pydub import AudioSegment

from patterns.result import Result


class AudioFormatter:

    SupportedFormats = ["wav", "mp3"]

    DefaultFormat = "wav"

    @staticmethod
    def __is_wav(filename):
        return filename.lower().endswith(".wav")

    @staticmethod
    def __get_format(filename) -> str:
        return filename.split(".")[-1]

    def __validate_format(filename) -> Result:
        format = AudioFormatter.__get_format(filename)

        if format not in AudioFormatter.SupportedFormats:
            return Result(None, f"Unsupported format: {format}")

        return Result(format, None)

    def as_wav(filename) -> Result:
        if AudioFormatter.__is_wav(filename):
            return Result(filename, None)
        wav_filename = filename.replace(
            AudioFormatter.__get_format(filename), AudioFormatter.DefaultFormat
        )
        return AudioFormatter.convert_to_wav(filename, wav_filename)

    @staticmethod
    def convert_to_wav(filename, wav_file) -> Result:
        """
        Converts an MP3 file to a WAV file.

        Parameters:
            filename (str): Path to the input MP3 file.
            wav_file (str): Path to the output WAV file.

        Returns:
            Result: A Result object containing the converted WAV file path on success,
            or an error message on failure.
        """
        if AudioFormatter.__is_wav(filename):
            return Result(wav_file, None)

        (_, err) = AudioFormatter.__validate_format(filename).unwrap()
        if err:
            return Result(None, err)

        # Load the MP3 file
        audio = AudioSegment.from_file(
            filename, format=AudioFormatter.__get_format(filename)
        )

        # Export as WAV
        audio.export(wav_file, format=AudioFormatter.DefaultFormat)

        return Result(wav_file, None)
