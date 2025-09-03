import React, { useState, useEffect } from 'react';
import axios from '../api/axios';
import { useNavigate } from 'react-router-dom';
import Container from '@mui/material/Container';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import MenuItem from '@mui/material/MenuItem';
import Alert from '@mui/material/Alert';

function InventaireForm() {
    const [materiel, setMateriel] = useState('');
    const [materiels, setMateriels] = useState([]);
    const [date, setDate] = useState('');
    const [quantite, setQuantite] = useState(1);
    const [error, setError] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        axios.get('/materiels/').then(res => setMateriels(res.data));
    }, []);

    const handleSubmit = (e) => {
        e.preventDefault();
        const data = { materiel, date, quantite };
        axios.post('/inventaires/', data)
            .then(() => navigate('/inventaires'))
            .catch(() => setError('Erreur lors de l\'enregistrement'));
    };

    return (
        <Container maxWidth="sm" sx={{ mt: 4 }}>
            <Box sx={{ p: 3, boxShadow: 2, borderRadius: 2, background: '#fff' }}>
                <Typography variant="h5" gutterBottom>Ajouter un inventaire</Typography>
                <form onSubmit={handleSubmit}>
                    <TextField
                        select fullWidth label="Matériel" value={materiel} onChange={e=>setMateriel(e.target.value)} sx={{mb:2}} required
                    >
                        {materiels.map(mat => (
                            <MenuItem key={mat.id} value={mat.id}>{mat.nom}</MenuItem>
                        ))}
                    </TextField>
                    <TextField
                        fullWidth label="Date" type="date" value={date} onChange={e=>setDate(e.target.value)} sx={{mb:2}} required
                        InputLabelProps={{ shrink: true }}
                    />
                    <TextField
                        fullWidth label="Quantité" type="number" value={quantite} onChange={e=>setQuantite(e.target.value)} sx={{mb:2}} required
                    />
                    <Button type="submit" variant="contained">Ajouter</Button>
                    {error && <Alert severity="error" sx={{mt:2}}>{error}</Alert>}
                </form>
            </Box>
        </Container>
    );
}

export default InventaireForm;