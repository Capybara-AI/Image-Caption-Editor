import streamlit as st
import json
import os
import sys


def load_captions(json_path):
    """Load captions from a JSON file."""
    with open(json_path, 'r') as file:
        captions = json.load(file)
    return captions

def save_corrected_caption(json_path, captions, image_name, new_caption):
    """Save the corrected caption and update the JSON file."""
    captions[image_name] = new_caption
    with open(json_path, 'w') as file:
        json.dump(captions, file, indent=4)
    return captions

def main():
    """Main function to run the Streamlit app."""
    st.markdown("<h1 style='text-align: center;'>Image Caption Editor</h1>", unsafe_allow_html=True)

    # User inputs for paths
    json_path = st.text_input('Enter the JSON file path:')
    image_folder = st.text_input('Enter the image folder path:')

    if os.path.exists(json_path) and os.path.isfile(json_path) and os.path.isdir(image_folder):
        captions = load_captions(json_path)
        total_images = len(captions)
        images_done = st.session_state.get('images_done', 0)

        if captions:
            image_name = st.selectbox('Select an image:', sorted(captions.keys()))
            if image_name:
                image_path = os.path.join(image_folder, image_name)
                if os.path.exists(image_path):
                    st.image(image_path, caption='Current Image', use_column_width=True, height=300)
                    new_caption = st.text_area('Edit the caption:', value=captions[image_name], height=250)

                    if st.button('Save Caption'):
                        captions = save_corrected_caption(json_path, captions, image_name, new_caption)
                        del captions[image_name]
                        st.session_state['images_done'] = images_done + 1
                        st.success(f'Caption for {image_name} saved successfully.')

                        if captions:
                            st.session_state['next_image'] = next(iter(captions))
                            st.experimental_rerun()
                        else:
                            st.write("All captions edited. No more images to display.")
                else:
                    st.error("The specified image does not exist in the given folder.")
            else:
                st.write("Select an image to edit its caption.")

            # Progress bar
            if total_images > 0:
                progress = images_done / total_images
                st.progress(progress)
                st.write(f"Edited {images_done} out of {total_images} images.")
        else:
            st.warning("No captions available in the JSON file. Please check the file content.")
    else:
        st.warning("Enter valid paths for the JSON file and image folder.")

if __name__ == "__main__":
    main()