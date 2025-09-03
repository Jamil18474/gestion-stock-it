import React, { useState, useEffect } from 'react';
import axios from '../api/axios';
import { useNavigate, useParams } from 'react-router-dom';
import Container from '@mui/material/Container';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Alert from '@mui/material/Alert';

function CategorieForm() {
    const [nom, setNom] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();
    const { id } = useParams();

    useEffect(() => {
        if (id) {
            axios.get(`/categories/${id}/`).then(res => setNom(res.data.nom));
        }
    }, [id]);

    const handleSubmit = (e) => {
        e.preventDefault();
        const data = { nom };
        const req = id
            ? axios.put(`/categories/${id}/`, data)
            : axios.post('/categories/', data);
        req
            .then(() => navigate('/categories'))
            .catch(() => setError('Erreur lors de l\'enregistrement'));
    };

    return (
        <Container maxWidth="sm" sx={{ mt: 4 }}>
            <Box sx={{ p: 3, boxShadow: 2, borderRadius: 2, background: '#fff' }}>
                <Typography variant="h5" gutterBottom>{id ? 'Modifier' : 'Ajouter'} une catégorie</Typography>
                <form onSubmit={handleSubmit}>
                    <TextField fullWidth label="Nom" value={nom} onChange={e=>setNom(e.target.value)} sx={{mb:2}} required />
                    <Button type="submit" variant="contained">{id ? 'Modifier' : 'Ajouter'}</Button>
                    {error && <Alert severity="error" sx={{mt:2}}>{error}</Alert>}
                </form>
            </Box>
        </Container>
    );
}

export default CategorieForm;