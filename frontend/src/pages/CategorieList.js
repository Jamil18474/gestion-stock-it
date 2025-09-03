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

function CategorieList() {
    const [categories, setCategories] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios.get('/categories/').then(res => setCategories(res.data)).finally(() => setLoading(false));
    }, []);

    const handleDelete = (id) => {
        if(window.confirm("Confirmer la suppression ?")) {
            axios.delete(`/categories/${id}/`).then(() => setCategories(categories.filter(c => c.id !== id)));
        }
    };

    return (
        <Container maxWidth="md" sx={{ mt: 4 }}>
            <Typography variant="h4" gutterBottom>Catégories</Typography>
            <Button
                variant="contained"
                color="primary"
                component={Link}
                to="/categories/add"
                sx={{ mb: 2 }}
            >
                Ajouter une catégorie
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
                                    <TableCell>Actions</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {categories.map((cat) => (
                                    <TableRow key={cat.id}>
                                        <TableCell>{cat.nom}</TableCell>
                                        <TableCell>
                                            <Button
                                                size="small"
                                                variant="outlined"
                                                color="secondary"
                                                component={Link}
                                                to={`/categories/${cat.id}/edit`}
                                                sx={{ mr: 1 }}
                                            >Modifier</Button>
                                            <Button
                                                size="small"
                                                variant="outlined"
                                                color="error"
                                                onClick={() => handleDelete(cat.id)}
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

export default CategorieList;