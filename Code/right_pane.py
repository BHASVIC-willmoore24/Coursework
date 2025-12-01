from PySide6.QtWidgets import (
    QPushButton,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QSlider
)

from PySide6.QtCore import (
        Qt,
        QUrl,
        QTime
)

from PySide6.QtGui import (
        QPixmap,
)

from PySide6.QtMultimedia import (
        QMediaPlayer,
        QAudioOutput
)

class RightPane(QMainWindow):
    def __init__(self, lyrics, credit, recommendations):
        super().__init__()
        self.lyrics = lyrics
        self.credits = credit
        self.recommendations = recommendations

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)

        # display album cover
        self.album_cover_label = QLabel("Nothing Playing")
        self.album_cover_label.setAlignment(Qt.AlignCenter)
        self.album_cover_label.setFixedSize(300, 300)
        self.album_cover_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # for information i.e. title, artist album
        info_widget = QWidget()
        info_layout = QVBoxLayout()
        info_widget.setLayout(info_layout)
        info_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        info_widget.setMaximumWidth(250)

        self.title_label = QLabel("Track Name")
        self.title_label.setWordWrap(True)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.artist_label = QLabel("Artist")
        self.artist_label.setWordWrap(True)
        self.artist_label.setAlignment(Qt.AlignCenter)

        self.album_name_label = QLabel("Album")
        self.album_name_label.setWordWrap(True)
        self.album_name_label.setAlignment(Qt.AlignCenter)

        # progress bar
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        self.current_time = QLabel("00:00")
        self.final_time = QLabel("00:00")

        slider_layout = QHBoxLayout()
        slider_layout.addWidget(self.current_time)
        slider_layout.addWidget(self.slider)
        slider_layout.addWidget(self.final_time)

        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play_pause)

        self.layout.addWidget(self.album_cover_label)
        info_layout.addWidget(self.title_label)
        info_layout.addWidget(self.artist_label)
        info_layout.addWidget(self.album_name_label)
        self.layout.addWidget(info_widget)
        self.layout.addSpacing(30)
        self.layout.addLayout(slider_layout)
        self.layout.addWidget(self.play_button)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        # play audio
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        # update play/pause button text
        self.player.playbackStateChanged.connect(self.update_playpause)

        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.duration_changed)

    # play or pause music
    def play_pause(self):
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    # change text of play/pause button
    def update_playpause(self, is_playpause):
        if is_playpause == QMediaPlayer.PlaybackState.PlayingState:
            self.play_button.setText("Pause")
        else:
            self.play_button.setText("Play")

    # method called in library
    def current_track(self, track):
        path = track[0]
        # ensure correct data type (string not list)
        artist = " ".join(track[1]) if isinstance(track[1], list) else str(track[1])
        album = " ".join(track[2]) if isinstance(track[2], list) else str(track[2])
        title = " ".join(track[3]) if isinstance(track[3], list) else str(track[3])
        mb_id = " ".join(track[9] if isinstance(track[9], list) else str(track[9]))
        genre = " ".join(track[6] if isinstance(track[6], list) else str(track[6]))
        album_cover_path = track[8]

        self.title_label.setText(title)
        self.artist_label.setText(artist)
        self.album_name_label.setText(album)

        pixmap = QPixmap(album_cover_path)
        pixmap = pixmap.scaled(
                self.album_cover_label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
        )
        self.album_cover_label.setPixmap(pixmap)

        # sets the source of the player as the correct path
        self.player.setSource(QUrl.fromLocalFile(path))
        self.player.play()

        length = track[7]
        self.lyrics.searching(artist, title, album, length)
        self.credits.searching(mb_id)
        self.recommendations.get_recommendations(track, artist, album, genre)

    # position_changed and duration_changed are for using the progress bar
    def position_changed(self, position):
        if not self.slider.isSliderDown():
            self.slider.setValue(position)

        self.current_time.setText(self.format_time(position))

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)
        self.final_time.setText(self.format_time(duration))

    def set_position(self, position):
        self.player.setPosition(position)

    # convert miliseconds to the correct format
    def format_time(self, ms):
        seconds = (ms // 1000) % 60
        minutes = ms // 60000
        return f"{minutes:02}:{seconds:02}"



