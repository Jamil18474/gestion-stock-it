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

function MouvementList() {
    const [mouvements, setMouvements] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios.get('/mouvements/').then(res => setMouvements(res.data)).finally(() => setLoading(false));
    }, []);

    const typeColor = (type) => {
        if (type === 'entree') return 'success';
        if (type === 'sortie') return 'error';
        if (type === 'transfert') return 'warning';
        return 'default';
    };

    return (
        <Container maxWidth="lg" sx={{ mt: 4 }}>
            <Typography variant="h4" gutterBottom>Mouvements</Typography>
            <Button
                variant="contained"
                color="primary"
                component={Link}
                to="/mouvements/add"
                sx={{ mb: 2 }}
            >
                Ajouter un mouvement
            </Button>
            <Box sx={{ boxShadow: 2, borderRadius: 2, background: '#fff', p: 2 }}>
                {loading ? (
                    <Typography>Chargement...</Typography>
                ) : (
                    <TableContainer component={Paper}>
                        <Table>
                            <TableHead>
                                <TableRow>
                                    <TableCell>Matériel</TableCell>
                                    <TableCell>Type</TableCell>
                                    <TableCell>Quantité</TableCell>
                                    <TableCell>Date</TableCell>
                                    <TableCell>Opérateur</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {mouvements.map((m) => (
                                    <TableRow key={m.id}>
                                        <TableCell>{m.materiel_nom || m.materiel}</TableCell>
                                        <TableCell>
                                            <Chip label={m.type} color={typeColor(m.type)} />
                                        </TableCell>
                                        <TableCell>{m.quantite}</TableCell>
                                        <TableCell>{m.date ? new Date(m.date).toLocaleString() : '-'}</TableCell>
                                        <TableCell>{m.operateur_username || m.operateur}</TableCell>
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

export default MouvementList;