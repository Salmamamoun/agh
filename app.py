import streamlit as st 
col1, col2, col3 = st.columns(3)

with col1:
    st.title(' Hillu buddy !!')

with col2:
    from PIL import Image
    image = Image.open('winktwin.jpg')
    st.image(image, caption=" wink wink ;) ",width=230)

with col3:
    question = st.radio("Do you want to go on a date with me : ", ('YESSSS', 'Nah thanks'))
    if (question == 'YESSSS'):
        st.success('YESSSS')
    else:
        st.success("C moooon , think again!!")

    date_ideas = st.multiselect("Date Ideas : ",
                            ['Dancing under the rain', 'Starring at the ceiling together', 'Talking about philosophy'])

    st.write("For more info contact me via email : mamounsalma23@gmail.com") 
