package br.edu.iftm.ds.exemplos.imobiliaria.repository;


import br.edu.iftm.ds.exemplos.imobiliaria.domain.Visita ;
import org.springframework.data.jpa.repository.JpaRepository;

public interface VisitaRepository   extends JpaRepository<Visita , Integer> {
}
