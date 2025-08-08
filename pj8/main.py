import streamlit as st
st.set_page_config(page_title='Ca sĩ yêu thích',page_icon='question:', layout='wide')
with st.sidebar:
    image='pj8/Minhvuong.png'
    st.image(image, caption='Minh Vương M4U')
    st.write('Họ và tên: Trần Thương Minh Vương')
    st.write('Nghệ danh: Minh Vương M4U')
    st.write('Trần Trương Minh Vương (sinh ngày 21 tháng 12 năm 1984), thường được biết tới đơn giản là Minh Vương (hay còn gọi là Minh Vương M4U) là nam ca sĩ và nhạc sĩ nhạc trẻ của Việt Nam, có sở trường về nhạc pop ballad.')
st.title('Bài hát yêu thích')
st.write('Trúc xinh (Remix)')
audio=open('pj8/Trucxinh.mp3','rb')
st.audio('Trucxinh.mp3',format='mp3')
st.title('MV yêu thích')
video='https://www.youtube.com/watch?v=EHASipZkZnk&list=RDEHASipZkZnk&start_radio=1&pp=ygURZW0gxqFpIGzDqm4gcGjhu5GgBwE%3D'
st.video(video,format='mp4/video')


