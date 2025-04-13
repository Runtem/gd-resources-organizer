import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# List of Geometry Dash level names without spaces
LEVEL_NAMES = [
    "StereoMadness", "BackOnTrack", "Polargeist", "DryOut", "BaseAfterBase",
    "CantLetGo", "Jumper", "TimeMachine", "Cycles", "xStep", "Clutterfunk",
    "TheoryOfEverything", "Electroman", "Clubstep", "Electrodynamix", "HexagonForce",
    "BlastProcessing", "TheoryOfEverything2", "GeometricalDominator", "Deadlocked",
    "Fingerdash", "Dash"  # Added Dash for Geometry Dash 2.2
]

DEFAULT_SOURCE_DIR = r"C:\SteamLibrary\steamapps\common\Geometry Dash\Resources"

def organize_resources(source_dir, destination_dir):
    # Music
    music_folder = os.path.join(destination_dir, "Music")
    other_music_folder = os.path.join(music_folder, "Other Music")
    official_nongs_folder = os.path.join(music_folder, "Official NONGs")  # Renamed from Custom Music
    os.makedirs(other_music_folder, exist_ok=True)
    os.makedirs(official_nongs_folder, exist_ok=True)

    # Copy official Geometry Dash level music
    for level in LEVEL_NAMES:
        level_file = f"{level}.mp3"  # No spaces in level names
        level_path = os.path.join(source_dir, level_file)
        if os.path.exists(level_path):
            shutil.copy(level_path, music_folder)
            print(f"Copied {level_file} to Music folder.")
        else:
            print(f"File {level_file} not found in source directory.")

    # Copy custom songs (not official levels)
    custom_songs = [
        "DJRubRub", "menuLoop", "secretLoop", "secretLoop02", "secretLoop03",
        "secretLoop04", "secretShop", "shop", "shop3", "shop4", "shop5", "StayInsideMe",
        "dangerLoop", "PowerTrip"  # Added dangerLoop and PowerTrip
    ]
    for song in custom_songs:
        # Handle secretLoop04 as an OGG file
        if song == "secretLoop04":
            song_file = f"{song}.ogg"
        else:
            song_file = f"{song}.mp3"

        song_path = os.path.join(source_dir, song_file)
        if os.path.exists(song_path):
            shutil.copy(song_path, other_music_folder)
            print(f"Copied {song_file} to Other Music folder.")
        else:
            print(f"File {song_file} not found in source directory.")

    # Copy files from the "songs" subfolder into Official NONGs
    songs_subfolder = os.path.join(source_dir, "songs")  # Changed from "music" to "songs"
    if os.path.exists(songs_subfolder):
        for file in os.listdir(songs_subfolder):
            src_path = os.path.join(songs_subfolder, file)
            shutil.copy(src_path, official_nongs_folder)
            print(f"Copied {file} to Official NONGs folder.")
    else:
        print("The 'songs' subfolder was not found in the source directory.")

    # Backgrounds and Foregrounds
    foregrounds_folder = os.path.join(destination_dir, "Foregrounds")
    backgrounds_folder = os.path.join(destination_dir, "Backgrounds")
    os.makedirs(foregrounds_folder, exist_ok=True)
    os.makedirs(backgrounds_folder, exist_ok=True)
    for file in os.listdir(source_dir):
        if file.startswith("fg_"):
            shutil.copy(os.path.join(source_dir, file), foregrounds_folder)
            print(f"Copied {file} to Foregrounds folder.")
        elif file.startswith("game_bg"):  # Corrected from "game_bj" to "game_bg"
            shutil.copy(os.path.join(source_dir, file), backgrounds_folder)
            print(f"Copied {file} to Backgrounds folder.")

    # Game Sheets
    game_sheets_folder = os.path.join(destination_dir, "Game Sheets")
    os.makedirs(game_sheets_folder, exist_ok=True)
    game_sheet_prefixes = ["GJ_GameSheet", "GJ_ShopSheet", "GJ_LaunchSheet", "GJ_PathSheet", "GJ_PixelSheet", "SecretSheet"]
    for file in os.listdir(source_dir):
        if any(file.startswith(prefix) for prefix in game_sheet_prefixes) and not file.endswith(".plist"):
            shutil.copy(os.path.join(source_dir, file), game_sheets_folder)
            print(f"Copied {file} to Game Sheets folder.")

    # Fonts
    fonts_folder = os.path.join(destination_dir, "Fonts")
    typeable_fonts_folder = os.path.join(fonts_folder, "Typeable Fonts")
    font_pngs_folder = os.path.join(fonts_folder, "Font PNGs")
    os.makedirs(typeable_fonts_folder, exist_ok=True)
    os.makedirs(font_pngs_folder, exist_ok=True)
    font_prefixes = ["gjFont", "bigFont", "chatFont"]
    for file in os.listdir(source_dir):
        if any(file.startswith(prefix) for prefix in font_prefixes):
            if file.endswith(".fnt"):
                shutil.copy(os.path.join(source_dir, file), typeable_fonts_folder)
                print(f"Copied {file} to Typeable Fonts folder.")
            elif file.endswith(".png"):
                shutil.copy(os.path.join(source_dir, file), font_pngs_folder)
                print(f"Copied {file} to Font PNGs folder.")

    # Sound Effects (SFX)
    sfx_folder = os.path.join(destination_dir, "SFX")
    custom_sfx_folder = os.path.join(destination_dir, "Custom SFX")
    os.makedirs(sfx_folder, exist_ok=True)
    os.makedirs(custom_sfx_folder, exist_ok=True)

    # List of predefined sound effects
    predefined_sfx = [
        "achievement_01", "buyItem01", "buyItem03", "chest07", "chest08", "chestClick", "chestLand",
        "chestOpen01", "counter003", "crystal01", "door001", "door01", "door02", "endStart_02",
        "explode_11", "gold01", "gold02", "grunt01", "grunt02", "grunt03", "highscoreGet02",
        "magicExplosion", "playSound_01", "quitSound_01", "reward01", "secretKey", "unlockPath"
    ]

    # Copy predefined SFX files (.ogg) to the SFX folder
    for sfx_name in predefined_sfx:
        sfx_file = f"{sfx_name}.ogg"
        sfx_path = os.path.join(source_dir, sfx_file)
        if os.path.exists(sfx_path):
            shutil.copy(sfx_path, sfx_folder)
            print(f"Copied {sfx_file} to SFX folder.")
        else:
            print(f"File {sfx_file} not found in source directory.")

    # Copy all files from the "sfx" subfolder to Custom SFX
    sfx_subfolder = os.path.join(source_dir, "sfx")
    if os.path.exists(sfx_subfolder):
        for file in os.listdir(sfx_subfolder):
            src_path = os.path.join(sfx_subfolder, file)
            shutil.copy(src_path, custom_sfx_folder)
            print(f"Copied {file} to Custom SFX folder.")
    else:
        print("The 'sfx' subfolder was not found in the source directory.")

    # Icons
    icons_folder = os.path.join(destination_dir, "Icons")
    ufo_folder = os.path.join(icons_folder, "UFO")
    wave_folder = os.path.join(icons_folder, "Wave")
    jetpack_folder = os.path.join(icons_folder, "Jetpack")
    cube_folder = os.path.join(icons_folder, "Cube")
    ball_folder = os.path.join(icons_folder, "Ball")
    robot_folder = os.path.join(icons_folder, "Robot")
    ship_folder = os.path.join(icons_folder, "Ship")
    spider_folder = os.path.join(icons_folder, "Spider")
    swing_folder = os.path.join(icons_folder, "Swing")

    # Create subfolders for icons
    os.makedirs(ufo_folder, exist_ok=True)
    os.makedirs(wave_folder, exist_ok=True)
    os.makedirs(jetpack_folder, exist_ok=True)
    os.makedirs(cube_folder, exist_ok=True)
    os.makedirs(ball_folder, exist_ok=True)
    os.makedirs(robot_folder, exist_ok=True)
    os.makedirs(ship_folder, exist_ok=True)
    os.makedirs(spider_folder, exist_ok=True)
    os.makedirs(swing_folder, exist_ok=True)

    # Copy files from the "icons" subfolder into their respective categories
    icons_subfolder = os.path.join(source_dir, "icons")
    if os.path.exists(icons_subfolder):
        for file in os.listdir(icons_subfolder):
            src_path = os.path.join(icons_subfolder, file)

            # Determine the destination folder based on the file prefix
            if file.startswith("bird"):
                dst_path = os.path.join(ufo_folder, file)
            elif file.startswith("dart"):
                dst_path = os.path.join(wave_folder, file)
            elif file.startswith("jetpack"):
                dst_path = os.path.join(jetpack_folder, file)
            elif file.startswith("player_ball"):
                dst_path = os.path.join(ball_folder, file)
            elif file.startswith("player"):
                dst_path = os.path.join(cube_folder, file)
            elif file.startswith("robot"):
                dst_path = os.path.join(robot_folder, file)
            elif file.startswith("ship"):
                dst_path = os.path.join(ship_folder, file)
            elif file.startswith("spider"):
                dst_path = os.path.join(spider_folder, file)
            elif file.startswith("swing"):
                dst_path = os.path.join(swing_folder, file)
            else:
                dst_path = os.path.join(icons_folder, file)  # Default to the main Icons folder

            # Copy the file to its correct location
            shutil.copy(src_path, dst_path)
            print(f"Copied {file} to {dst_path}.")
    else:
        print("The 'icons' subfolder was not found in the source directory.")

def unorganize_resources(source_dir, destination_dir):
    # Ensure necessary subfolders exist in the destination directory
    songs_subfolder = os.path.join(destination_dir, "songs")  # For Official NONGs
    sfx_subfolder = os.path.join(destination_dir, "sfx")      # For Custom SFX
    icons_subfolder = os.path.join(destination_dir, "icons")  # For Icons
    os.makedirs(songs_subfolder, exist_ok=True)
    os.makedirs(sfx_subfolder, exist_ok=True)
    os.makedirs(icons_subfolder, exist_ok=True)

    # Walk through the organized source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            src_path = os.path.join(root, file)

            # Determine the destination path based on the folder structure
            if "Custom SFX" in root:  # Files from Custom SFX go to the 'sfx' subfolder
                dst_path = os.path.join(sfx_subfolder, file)
            elif "Official NONGs" in root:  # Files from Official NONGs go to the 'songs' subfolder
                dst_path = os.path.join(songs_subfolder, file)
            elif "Other Music" in root:  # Files from Other Music go to the root of the destination
                dst_path = os.path.join(destination_dir, file)
            elif "Music" in root:  # Official level music goes to the root of the destination
                dst_path = os.path.join(destination_dir, file)
            elif "Foregrounds" in root:  # Foreground files go to the root of the destination
                dst_path = os.path.join(destination_dir, file)
            elif "Backgrounds" in root:  # Background files go to the root of the destination
                dst_path = os.path.join(destination_dir, file)
            elif "Game Sheets" in root:  # Game sheet files go to the root of the destination
                dst_path = os.path.join(destination_dir, file)
            elif "Fonts" in root:  # Font files go to the root of the destination
                dst_path = os.path.join(destination_dir, file)
            elif "Icons" in root:  # Icon files go to the 'icons' subfolder
                dst_path = os.path.join(icons_subfolder, file)
            else:  # All other files go to the root of the destination
                dst_path = os.path.join(destination_dir, file)

            # Copy the file to its correct location
            shutil.copy(src_path, dst_path)
            print(f"Copied {file} back to {dst_path}.")

def main():
    def select_source_directory():
        source_dir = filedialog.askdirectory(title="Select Source Directory")
        if source_dir:
            source_entry.delete(0, tk.END)
            source_entry.insert(0, source_dir)

    def select_destination_directory():
        destination_dir = filedialog.askdirectory(title="Select Destination Directory")
        if destination_dir:
            destination_entry.delete(0, tk.END)
            destination_entry.insert(0, destination_dir)

    def on_submit():
        source_dir = source_entry.get()
        destination_dir = destination_entry.get()
        action = action_var.get()

        if not os.path.exists(source_dir):
            messagebox.showwarning("Invalid Source", "The source directory does not exist.")
            return
        if not os.path.exists(destination_dir):
            messagebox.showwarning("Invalid Destination", "The destination directory does not exist.")
            return

        try:
            if action == "Organize":
                organize_resources(source_dir, destination_dir)
            elif action == "Unorganize":
                unorganize_resources(source_dir, destination_dir)
            messagebox.showinfo("Success", f"Resources have been {action.lower()}d successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    root = tk.Tk()
    root.title("Geometry Dash Resource Organizer")

    tk.Label(root, text="Source Directory:").grid(row=0, column=0, padx=5, pady=5)
    source_entry = tk.Entry(root, width=50)
    source_entry.grid(row=0, column=1, padx=5, pady=5)
    source_entry.insert(0, DEFAULT_SOURCE_DIR)
    tk.Button(root, text="Browse", command=select_source_directory).grid(row=0, column=2, padx=5, pady=5)

    tk.Label(root, text="Destination Directory:").grid(row=1, column=0, padx=5, pady=5)
    destination_entry = tk.Entry(root, width=50)
    destination_entry.grid(row=1, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=select_destination_directory).grid(row=1, column=2, padx=5, pady=5)

    tk.Label(root, text="Action:").grid(row=2, column=0, padx=5, pady=5)
    action_var = tk.StringVar(value="Organize")
    tk.OptionMenu(root, action_var, "Organize", "Unorganize").grid(row=2, column=1, padx=5, pady=5)

    tk.Button(root, text="Start", command=on_submit).grid(row=3, column=1, padx=5, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()