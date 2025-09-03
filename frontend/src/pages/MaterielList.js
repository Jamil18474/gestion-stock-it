import React, { useEffect, useState } from 'react';
import axios from '../api/axios';
import { Link } from 'react-router-dom';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Chip from '@mui/material/Chip';

function MaterielList() {
    const [materiels, setMateriels] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios.get('/materiels/').then(res => setMateriels(res.data)).finally(() => setLoading(false));
    }, []);

    const etatColor = (etat) => {
        if (etat === 'neuf') return 'success';
        if (etat === 'utilisé') return 'warning';
        if (etat === 'HS' || etat === 'hors service') return 'error';
        return 'default';
    };

    const handleDelete = (id) => {
        if(window.confirm("Confirmer la suppression ?")) {
            axios.delete(`/materiels/${id}/`).then(() => setMateriels(materiels.filter(m => m.id !== id)));
        }
    };

    return (
        <Container maxWidth="lg" sx={{ mt: 4 }}>
            <Typography variant="h4" gutterBottom>Matériels</Typography>
            <Button
                variant="contained"
                color="primary"
                component={Link}
                to="/materiels/add"
                sx={{ mb: 2 }}
            >
                Ajouter un matériel
            </Button>
            <Box sx={{ boxShadow: 2, borderRadius: 2, background: '#fff', p: 2 }}>
                {loading ? (
                    <Typography>Chargement...</Typography>
                ) : (
                    <TableContainer component={Paper}>
                        <Table>
                            <TableHead>
                                <TableRow>
                                    <TableCell>Nom</TableCell>
                                    <TableCell>Référence</TableCell>
                                    <TableCell>Catégorie</TableCell>
                                    <TableCell>État</TableCell>
                                    <TableCell>Date d'achat</TableCell>
                                    <TableCell>Localisation</TableCell>
                                    <TableCell>Actions</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {materiels.map((mat) => (
                                    <TableRow key={mat.id}>
                                        <TableCell>{mat.nom}</TableCell>
                                        <TableCell>{mat.reference}</TableCell>
                                        <TableCell>{mat.categorie_nom || mat.categorie}</TableCell>
                                        <TableCell>
                                            <Chip label={mat.etat} color={etatColor(mat.etat)} />
                                        </TableCell>
                                        <TableCell>{mat.date_achat ? new Date(mat.date_achat).toLocaleDateString() : '-'}</TableCell>
                                        <TableCell>{mat.localisation}</TableCell>
                                        <TableCell>
                                            <Button
                                                size="small"
                                                variant="outlined"
                                                color="secondary"
                                                component={Link}
                                                to={`/materiels/${mat.id}/edit`}
                                                sx={{ mr: 1 }}
                                            >Modifier</Button>
                                            <Button
                                                size="small"
                                                variant="outlined"
                                                color="error"
                                                onClick={() => handleDelete(mat.id)}
                                            >Supprimer</Button>
                                        </TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </TableContainer>
                )}
            </Box>
        </Container>
    );
}

export default MaterielList;