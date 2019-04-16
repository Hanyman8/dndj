import pytest

from src.music import Track, TrackList


class TestTrackList:

    @pytest.fixture
    def minimal_track_list_config(self):
        return {
            "name": "Some Name",
            "tracks": []
        }

    def test_minimal_dict_as_config(self, minimal_track_list_config):
        track_list = TrackList(minimal_track_list_config)
        assert track_list.name == "Some Name"
        assert len(track_list.tracks) == 0

    def test_tracks_are_created(self, minimal_track_list_config):
        minimal_track_list_config["tracks"] = [
            "some-filename.mp3",
            "other-filename.mp3"
        ]
        track_list = TrackList(minimal_track_list_config)
        assert len(track_list.tracks) == 2
        assert track_list.tracks[0] == Track("some-filename.mp3")
        assert track_list.tracks[1] == Track("other-filename.mp3")

    def test_directory_is_none_by_default(self, minimal_track_list_config):
        track_list = TrackList(minimal_track_list_config)
        assert track_list.directory is None

    def test_directory_in_config(self, minimal_track_list_config):
        minimal_track_list_config["directory"] = "/some/dir/"
        track_list = TrackList(minimal_track_list_config)
        assert track_list.directory == "/some/dir/"

    def test_loop_is_true_by_default(self, minimal_track_list_config):
        track_list = TrackList(minimal_track_list_config)
        assert track_list.loop is True

    def test_loop_in_config(self, minimal_track_list_config):
        minimal_track_list_config["loop"] = False
        track_list = TrackList(minimal_track_list_config)
        assert track_list.loop is False

    def test_shuffle_is_true_by_default(self, minimal_track_list_config):
        track_list = TrackList(minimal_track_list_config)
        assert track_list.shuffle is True

    def test_shuffle_in_config(self, minimal_track_list_config):
        minimal_track_list_config["shuffle"] = False
        track_list = TrackList(minimal_track_list_config)
        assert track_list.shuffle is False

    def test_tracks_use_tuple_instead_of_list(self, minimal_track_list_config):
        track_list = TrackList(minimal_track_list_config)
        assert isinstance(track_list.tracks, tuple)