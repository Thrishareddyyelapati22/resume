import streamlit as st
def main():


    st.title('My Portfolio')
    st.markdown('''Happy to share my resume- As learning goes on ,updations happen!:balloon: ''')
    
    st.sidebar.title(":blue[It's] :blue[me] :blue[Thrisha reddy]")

    page=st.sidebar.radio("Here you can check",("About me","Resume here","Contact"))

    if page=="About me":
            st.header(':green[About Me]')
            st.write(':blue[Good Morning Everyone !]')
            st.write("Myself Thrisha Reddy Yelapati")
            st.write("I am a Student Studying B.Tech 3rd year(Undergrad).Passionate about Working on interesting models and analayis.I beileve working with a team creates new ideas and these needs actions")
    if page=="Resume here":
            with open("MYRESUME.pdf","rb") as file:
               btn=st.download_button(
               label="Download My Resume",
               data=file,
               file_name="MYRESUME.pdf",
            )
    
    if page=="Contact":
            st.header('Contact')
            st.write('Contact information: thrishareddyyelapati@gmail.com')
            st.markdown('<i class="fas fa-phone-alt"></i> Phone: 9392704506', unsafe_allow_html=True)

   
            st.markdown('<i class="fab fa-linkedin"></i> LinkedIn: [Please Check out my Linkedln profile here](https://www.linkedin.com/in/thrishayelapati2203/)', unsafe_allow_html=True)

            st.markdown('<i class="fab fa-github"></i> GitHub:[My GitHub Profile](https://github.com/Thrishareddyyelapati22)', unsafe_allow_html=True)
            

            if st.button(":green[Thanks for viewing]"):
                st.balloons()  


if __name__ == '__main__':
    main()