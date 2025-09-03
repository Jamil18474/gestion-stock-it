import React from 'react';
import { Link } from 'react-router-dom';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardActionArea from '@mui/material/CardActionArea';

const dashboardLinks = [
    {
        title: "Matériels",
        description: "Consultez la liste des matériels et gérez leur inventaire.",
        to: "/materiels"
    },
    {
        title: "Catégories",
        description: "Gérez les catégories de matériels.",
        to: "/categories"
    },
    {
        title: "Mouvements",
        description: "Voir et enregistrer les entrées, sorties ou transferts de matériels.",
        to: "/mouvements"
    },
    {
        title: "Inventaires",
        description: "Consultez les inventaires et ajoutez de nouveaux états.",
        to: "/inventaires"
    }
];

function Dashboard() {
    return (
        <Container maxWidth="md" sx={{ mt: 4 }}>
            <Typography variant="h3" gutterBottom>
                Tableau de bord Stock IT
            </Typography>
            <Typography variant="body1" sx={{ mb: 4 }}>
                Utilisez le tableau de bord pour accéder rapidement aux différentes fonctionnalités du logiciel.
            </Typography>
            <Grid container spacing={4}>
                {dashboardLinks.map((link) => (
                    <Grid item xs={12} sm={6} key={link.to}>
                        <Card>
                            <CardActionArea component={Link} to={link.to}>
                                <CardContent>
                                    <Typography variant="h5" gutterBottom>
                                        {link.title}
                                    </Typography>
                                    <Typography variant="body2" color="text.secondary">
                                        {link.description}
                                    </Typography>
                                </CardContent>
                            </CardActionArea>
                        </Card>
                    </Grid>
                ))}
            </Grid>
        </Container>
    );
}

export default Dashboard;