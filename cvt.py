import json
import sys

def convert_to_srt(data):
    srt_output = ""
    for index, item in enumerate(data["body"]):
        start_time = int(item["from"] * 1000)
        end_time = int(item["to"] * 1000)
        content = item["content"]

        # Format timestamps
        start_time_formatted = f"{start_time // 3600000:02d}:{(start_time % 3600000) // 60000:02d}:{(start_time % 60000) // 1000:02d},{start_time % 1000:03d}"
        end_time_formatted = f"{end_time // 3600000:02d}:{(end_time % 3600000) // 60000:02d}:{(end_time % 60000) // 1000:02d},{end_time % 1000:03d}"

        # Add to SRT output
        srt_output += f"{index + 1}\n{start_time_formatted} --> {end_time_formatted}\n{content}\n\n"
    return srt_output

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]

    with open(input_file_path, "r") as input_file:
        data = json.load(input_file)

    srt_output = convert_to_srt(data)

    with open("output.srt", "w") as output_file:
        output_file.write(srt_output)

if __name__ == "__main__":
    main()

