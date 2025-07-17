import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# Load and normalize remedies dataset
df_remedies = pd.read_csv("home_remedies.csv")
df_remedies['Health Issue'] = df_remedies['Health Issue'].str.lower().str.strip()

# Title and intro
st.title("🩺 Health Tracker - Doctor’s Assistant")
st.markdown("Track 50+ diseases with trusted home remedies, yogasan tips, and doctor-assured prescriptions.")

# Dropdown
disease_options = df_remedies['Health Issue'].dropna().unique()
disease = st.selectbox("🦠 Choose a health issue:", sorted(disease_options))

# Mapping remedy names to prescription keys
remedy_to_prescription = {
    "diabetes": "diabetes", "hypertension": "hypertension", "asthma": "asthma", "fever": "fever",
    "cold": "cold", "cough": "cough", "headache": "headache", "migraine": "migraine", "indigestion": "indigestion",
    "acidity": "acidity", "constipation": "constipation", "diarrhea": "diarrhea", "vomiting": "vomiting",
    "typhoid": "typhoid", "dengue": "dengue", "malaria": "malaria", "chickenpox": "chickenpox",
    "eczema": "eczema", "psoriasis": "psoriasis", "arthritis": "arthritis", "rheumatoid arthritis": "rheumatoid arthritis",
    "back pain": "back pain", "sinusitis": "sinusitis", "bronchitis": "bronchitis", "pneumonia": "pneumonia",
    "tuberculosis": "tuberculosis", "covid-19": "covid-19", "urinary tract infection": "urinary tract infection",
    "kidney stones": "kidney stones", "gout": "gout", "thyroid": "thyroid (hypo)", "anemia": "anemia",
    "menstrual cramps": "menstrual cramps", "pcos": "pcos", "acne": "acne", "obesity": "obesity",
    "depression": "depression", "anxiety": "anxiety", "insomnia": "insomnia", "epilepsy": "epilepsy",
    "parkinson's": "parkinson's", "alzheimer's": "alzheimer's", "hepatitis": "hepatitis",
    "liver cirrhosis": "liver cirrhosis", "cholesterol": "cholesterol", "heart disease": "heart disease",
    "stroke": "stroke", "eye infection": "eye infection", "conjunctivitis": "conjunctivitis"
}

# Prescription data
disease_to_medicine = {
    "diabetes": ["Metformin", "Glimepiride", "Insulin Glargine"],
    "hypertension": ["Amlodipine", "Losartan", "Lisinopril"],
    "asthma": ["Salbutamol", "Fluticasone", "Montelukast"],
    "fever": ["Paracetamol", "Ibuprofen"],
    "cold": ["Cetirizine", "Levocetirizine"],
    "cough": ["Dextromethorphan", "Ambroxol"],
    "headache": ["Paracetamol", "Aspirin"],
    "migraine": ["Sumatriptan", "Naproxen"],
    "indigestion": ["Pantoprazole", "Domperidone"],
    "acidity": ["Ranitidine", "Omeprazole"],
    "constipation": ["Lactulose", "Isabgol"],
    "diarrhea": ["ORS", "Loperamide"],
    "vomiting": ["Ondansetron", "Domperidone"],
    "typhoid": ["Cefixime", "Azithromycin"],
    "dengue": ["Paracetamol", "IV fluids"],
    "malaria": ["Artemether", "Lumefantrine"],
    "chickenpox": ["Acyclovir", "Paracetamol"],
    "eczema": ["Hydrocortisone", "Cetirizine"],
    "psoriasis": ["Calcipotriol", "Methotrexate"],
    "arthritis": ["Diclofenac", "Aceclofenac"],
    "rheumatoid arthritis": ["Methotrexate", "Sulfasalazine"],
    "back pain": ["Ibuprofen", "Tizanidine"],
    "sinusitis": ["Amoxicillin", "Xylometazoline"],
    "bronchitis": ["Azithromycin", "Salbutamol"],
    "pneumonia": ["Ceftriaxone", "Levofloxacin"],
    "tuberculosis": ["Isoniazid", "Rifampicin"],
    "covid-19": ["Paracetamol", "Favipiravir"],
    "urinary tract infection": ["Nitrofurantoin", "Ciprofloxacin"],
    "kidney stones": ["Tamsulosin", "Diclofenac"],
    "gout": ["Allopurinol", "Colchicine"],
    "thyroid (hypo)": ["Levothyroxine"],
    "anemia": ["Ferrous Sulfate", "Folic Acid"],
    "menstrual cramps": ["Mefenamic Acid", "Ibuprofen"],
    "pcos": ["Metformin", "Oral Contraceptives"],
    "acne": ["Clindamycin", "Benzoyl Peroxide"],
    "obesity": ["Orlistat", "Metformin"],
    "depression": ["Fluoxetine", "Sertraline"],
    "anxiety": ["Alprazolam", "Buspirone"],
    "insomnia": ["Zolpidem", "Melatonin"],
    "epilepsy": ["Carbamazepine", "Valproate"],
    "parkinson's": ["Levodopa", "Carbidopa"],
    "alzheimer's": ["Donepezil", "Memantine"],
    "hepatitis": ["Tenofovir", "Entecavir"],
    "liver cirrhosis": ["Lactulose", "Spironolactone"],
    "cholesterol": ["Atorvastatin", "Rosuvastatin"],
    "heart disease": ["Aspirin", "Clopidogrel"],
    "stroke": ["Aspirin", "Atorvastatin"],
    "eye infection": ["Moxifloxacin Eye Drops", "Tobramycin"],
    "conjunctivitis": ["Chloramphenicol", "Olopatadine"]
}

# Display content
if disease:
    result = df_remedies[df_remedies['Health Issue'] == disease.lower()]
    if not result.empty:
        st.success(f"✅ Details for: {disease.title()}")

        st.markdown("### 🌿 Home Remedy")
        st.info(result['Home Remedy'].values[0])

        st.markdown("### 🧘 Suggested Yogasan")
        st.success(result['Yogasan'].values[0])

        # Prescriptions
        selected_disease = disease.lower().strip()
        mapped_disease = remedy_to_prescription.get(selected_disease, None)

        st.markdown("### 💊 Doctor-Assured Prescription")
        if mapped_disease and mapped_disease in disease_to_medicine:
            for med in disease_to_medicine[mapped_disease]:
                st.write(f"• {med}")
        else:
            st.warning("We're working on adding prescriptions for this condition.")
            st.markdown("🔎 Meanwhile, you can explore our full prescription reference guide:")
            st.markdown("""
<a href="https://docs.google.com/document/d/1EAEPEIU0H1oSWybA2GNWqcODKRM5usSh" target="_blank">
📄 **View Prescription Guide (PDF)**
</a>
""", unsafe_allow_html=True)

    else:
        st.warning("Disease not found. Try another.")

# Hospital finder button
st.markdown("### 🏥 Need Medical Assistance Nearby?")
st.markdown("""
<a href="https://www.google.com/maps/search/hospitals+near+me" target="_blank">
  <button style='padding:10px 20px; background-color:#4CAF50; color:white; 
                 border:none; border-radius:8px; font-size:16px; cursor:pointer;'>
    🧭 Find Nearby Hospitals
  </button>
</a>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("❤️ Made with care by 👸JOYSHRI and 🤴ARSHATH")