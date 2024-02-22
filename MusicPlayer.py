import os
import sys
import pygame
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QListWidget, QLabel, QSizePolicy


class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Music Player')
        self.setGeometry(100, 100, 400, 300)

        self.play_button = QPushButton('Play')
        self.play_button.clicked.connect(self.play_music)

        self.pause_button = QPushButton('Pause')
        self.pause_button.clicked.connect(self.pause_music)

        self.stop_button = QPushButton('Stop')
        self.stop_button.clicked.connect(self.stop_music)

        self.open_button = QPushButton('Open')
        self.open_button.clicked.connect(self.open_file_dialog)

        self.playlist_label = QLabel('Playlist:')
        self.playlist = QListWidget()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.play_button)
        self.layout.addWidget(self.pause_button)
        self.layout.addWidget(self.stop_button)
        self.layout.addWidget(self.open_button)
        self.layout.addWidget(self.playlist_label)
        self.layout.addWidget(self.playlist)

        self.setLayout(self.layout)

        self.music_list = []

    def open_file_dialog(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.ExistingFiles)
        dialog.setNameFilter("Audio Files (*.mp3 *.ogg *.wav)")
        if dialog.exec_():
            file_names = dialog.selectedFiles()
            for file_name in file_names:
                self.music_list.append(file_name)
                self.playlist.addItem(os.path.basename(file_name))

    def play_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.load(self.music_list[self.playlist.currentRow()])
            pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()

    # Initialize pygame mixer
    pygame.mixer.init()

    sys.exit(app.exec_())
