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

function InventaireList() {
    const [inventaires, setInventaires] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios.get('/inventaires/').then(res => setInventaires(res.data)).finally(() => setLoading(false));
    }, []);

    return (
        <Container maxWidth="lg" sx={{ mt: 4 }}>
            <Typography variant="h4" gutterBottom>Inventaires</Typography>
            <Button
                variant="contained"
                color="primary"
                component={Link}
                to="/inventaires/add"
                sx={{ mb: 2 }}
            >
                Ajouter un inventaire
            </Button>
            <Box sx={{ boxShadow: 2, borderRadius: 2, background: '#fff', p: 2 }}>
                {loading ? (
                    <Typography>Chargement...</Typography>
                ) : (
                    <TableContainer component={Paper}>
                        <Table>
                            <TableHead>
                                <TableRow>
                                    <TableCell>Date</TableCell>
                                    <TableCell>Matériel</TableCell>
                                    <TableCell>Quantité</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {inventaires.map((inv) => (
                                    <TableRow key={inv.id}>
                                        <TableCell>{inv.date ? new Date(inv.date).toLocaleDateString() : '-'}</TableCell>
                                        <TableCell>{inv.materiel_nom || inv.materiel}</TableCell>
                                        <TableCell>{inv.quantite}</TableCell>
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

export default InventaireList;