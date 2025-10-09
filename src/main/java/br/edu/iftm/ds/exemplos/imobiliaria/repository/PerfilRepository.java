package br.edu.iftm.ds.exemplos.imobiliaria.repository;

import br.edu.iftm.ds.exemplos.imobiliaria.domain.Perfil;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PerfilRepository extends JpaRepository<Perfil, Integer> {
}
