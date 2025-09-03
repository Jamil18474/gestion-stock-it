import React, { useState, useEffect } from 'react';
import axios from '../api/axios';
import { useNavigate, useParams } from 'react-router-dom';
import Container from '@mui/material/Container';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import MenuItem from '@mui/material/MenuItem';
import Alert from '@mui/material/Alert';

function MaterielForm() {
    const [nom, setNom] = useState('');
    const [reference, setReference] = useState('');
    const [categorie, setCategorie] = useState('');
    const [categories, setCategories] = useState([]);
    const [etat, setEtat] = useState('neuf');
    const [dateAchat, setDateAchat] = useState('');
    const [localisation, setLocalisation] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();
    const { id } = useParams();

    useEffect(() => {
        axios.get('/categories/').then(res => setCategories(res.data));
        if (id) {
            axios.get(`/materiels/${id}/`).then(res => {
                setNom(res.data.nom);
                setReference(res.data.reference);
                setCategorie(res.data.categorie);
                setEtat(res.data.etat);
                setDateAchat(res.data.date_achat);
                setLocalisation(res.data.localisation);
            });
        }
    }, [id]);

    const handleSubmit = (e) => {
        e.preventDefault();
        const data = {
            nom,
            reference,
            categorie,
            etat,
            date_achat: dateAchat,
            localisation,
        };
        const req = id
            ? axios.put(`/materiels/${id}/`, data)
            : axios.post('/materiels/', data);
        req
            .then(() => navigate('/materiels'))
            .catch(() => setError('Erreur lors de l\'enregistrement'));
    };

    return (
        <Container maxWidth="sm" sx={{ mt: 4 }}>
            <Box sx={{ p: 3, boxShadow: 2, borderRadius: 2, background: '#fff' }}>
                <Typography variant="h5" gutterBottom>{id ? 'Modifier' : 'Ajouter'} un matériel</Typography>
                <form onSubmit={handleSubmit}>
                    <TextField fullWidth label="Nom" value={nom} onChange={e=>setNom(e.target.value)} sx={{mb:2}} required />
                    <TextField fullWidth label="Référence" value={reference} onChange={e=>setReference(e.target.value)} sx={{mb:2}} />
                    <TextField
                        select fullWidth label="Catégorie" value={categorie} onChange={e=>setCategorie(e.target.value)} sx={{mb:2}} required
                    >
                        {categories.map(cat => (
                            <MenuItem key={cat.id} value={cat.id}>{cat.nom}</MenuItem>
                        ))}
                    </TextField>
                    <TextField
                        select fullWidth label="État" value={etat} onChange={e=>setEtat(e.target.value)} sx={{mb:2}} required
                    >
                        <MenuItem value="neuf">Neuf</MenuItem>
                        <MenuItem value="utilisé">Utilisé</MenuItem>
                        <MenuItem value="HS">Hors service</MenuItem>
                    </TextField>
                    <TextField
                        fullWidth label="Date d'achat" type="date" value={dateAchat || ''} onChange={e=>setDateAchat(e.target.value)} sx={{mb:2}}
                        InputLabelProps={{ shrink: true }}
                    />
                    <TextField fullWidth label="Localisation" value={localisation} onChange={e=>setLocalisation(e.target.value)} sx={{mb:2}} />
                    <Button type="submit" variant="contained">{id ? 'Modifier' : 'Ajouter'}</Button>
                    {error && <Alert severity="error" sx={{mt:2}}>{error}</Alert>}
                </form>
            </Box>
        </Container>
    );
}

export default MaterielForm;