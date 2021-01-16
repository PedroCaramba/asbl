#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:58:57 2021

@author: jeanlouisdendal
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def main():
    username = st.sidebar.text_input("Nom d'utilisateur")
    password = st.sidebar.text_input("Mot de passe",type='password')
    
    if st.sidebar.checkbox("Connexion"):        
        if username=="BeauSite" and password=="42##":          
            st.title("a s b l")
            st.sidebar.subheader("Faites votre choix")
            
            choix = st.sidebar.selectbox("",( "",
                                    "Dons", 
                                    "Trésorerie",
                                    "Echéancier"))
                                    
            if choix == 'Dons': 
                st.markdown("**Les dons par année civile à l'exclusion des legs**.")
                data = {'Année':[2016, 2017, 2018, 2019, 2020], 'Montant-k€':[3146, 2999, 3480, 2604, 1969]}
                df = pd.DataFrame(data,columns=['Année','Montant-k€'],dtype=int)
                fig = px.bar(df, x ='Année',y='Montant-k€', color='Année') 
                st.plotly_chart(fig)
                st.dataframe(df)
                
                
                
            if choix == 'Trésorerie': 
                st.markdown("**La trésorerie au fil de l'eau - en milliers d'euros**.")
                data = {'Date':["30/06/2017", "30/06/2018", "30/06/2019", "30/06/2020", "31/12/2020"], 'Montant':[67, 63, 56, 62, 60]}
                df = pd.DataFrame(data,columns=['Date','Montant'])
                fig = px.bar(df, x ='Date',y='Montant', color='Date') 
                st.plotly_chart(fig)
                st.dataframe(df)
                
                
            if choix == 'Echéancier': 
                st.markdown("**Les principales échéances administratives**.")
                data = {'Echéance':["Février", "Mars", "Mars", "Octobre", "Décembre", "Décembre"], 
                        'Objet':["Attestations Dons","Taxe annuelle asbl", "UBO Confirmation", "Subside communauté française", "Greffe - Comptes annuels", "Déclaration à l'Impôt des Personnes Morales"]}
                df = pd.DataFrame(data,columns=['Echéance','Objet'])
                st.dataframe(df)


if __name__ == '__main__':
    main()
