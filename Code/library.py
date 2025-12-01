from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QSizePolicy,
    QScrollArea,
    QPushButton,
    QFrame
)

from PySide6.QtGui import (
    QPixmap,
)

from PySide6.QtCore import (
    Qt,
)


class Library(QMainWindow):
    def __init__(self, right_pane):
        super().__init__()
        self.layout = QVBoxLayout()
        self.right_pane = right_pane

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.main_widget = QWidget()
        self.main_widget_layout = QVBoxLayout(self.main_widget)
        self.main_widget_layout.setAlignment(Qt.AlignTop)
        self.scroll_area.setWidget(self.main_widget)
        self.setCentralWidget(self.scroll_area)

    # using a method to update library display so this can be called in other classes
    def update_library(self, track):

        # removes/clears all albums from library when updating
        while self.main_widget_layout.count():
            temp = self.main_widget_layout.takeAt(0)
            if temp.widget():
                temp.widget().deleteLater()


        main_layout = QVBoxLayout()
        size_policy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # if statement ensures only working on a list - so there is no error during loop
        if len(track) > 0:

            # loop through each track - each sub list
            for i in track:
                album_widget = QWidget()
                # consistent heights for each album/track
                album_widget.setFixedHeight(100)

                # album_layout is for the entire track, info_layout is for specific information: title, album, artist
                album_layout = QHBoxLayout(album_widget)
                album_layout.setContentsMargins(5, 5, 5, 5)
                info_layout = QVBoxLayout()
                
                # getting an image from the album cover path
                cover = QLabel(self)
                path = i[8]
                if path:
                    pixmap = QPixmap(path)
                    pixmap = pixmap.scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio,
                                           Qt.TransformationMode.SmoothTransformation)
                    cover.setPixmap(pixmap)
                else:
                    cover.setText("Cover not found")

                cover.setFixedSize(80, 80)
                album_layout.addWidget(cover)

                # stop information i.e. album name from taking up too much horizontal space with particularly long titles
                info_widget = QWidget()
                info_widget.setLayout(info_layout)
                info_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                info_widget.setMaximumWidth(250)

                title = QLabel(self)
                title.setText(" ".join(i[3]))
                title.setWordWrap(True)
                info_layout.addWidget(title)

                album = QLabel(self)
                album.setText(" ".join(i[2]))
                album.setWordWrap(True)
                info_layout.addWidget(album)

                artist = QLabel(self)
                artist.setText(" ".join(i[1]))
                artist.setWordWrap(True)
                info_layout.addWidget(artist)

                album_layout.addWidget(info_widget)


                play_track = QPushButton(self)
                play_track.setText("Play")
                play_track.setSizePolicy(size_policy)
                # button runs track_info method, sending the data of the current track as a parameter
                play_track.clicked.connect(lambda checked=False, t_info=i: self.track_info(t_info))

                album_layout.addWidget(play_track)

                self.main_widget_layout.addWidget(album_widget)

    # links to right_pane
    def track_info(self, trackinf):
        self.right_pane.current_track(trackinf)
