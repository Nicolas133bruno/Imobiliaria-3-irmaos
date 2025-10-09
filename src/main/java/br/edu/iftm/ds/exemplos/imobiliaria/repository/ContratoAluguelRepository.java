package br.edu.iftm.ds.exemplos.imobiliaria.repository;

import br.edu.iftm.ds.exemplos.imobiliaria.domain.ContratoAluguel;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ContratoAluguelRepository  extends JpaRepository<ContratoAluguel, Integer> {
}
