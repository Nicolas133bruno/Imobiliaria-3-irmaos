package br.edu.iftm.ds.exemplos.imobiliaria.repository;

import br.edu.iftm.ds.exemplos.imobiliaria.domain.StatusImovel ;
import org.springframework.data.jpa.repository.JpaRepository;

public interface StatusImovelRepository  extends JpaRepository<StatusImovel , Integer> {
}
