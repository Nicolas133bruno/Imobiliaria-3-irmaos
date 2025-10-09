package br.edu.iftm.ds.exemplos.imobiliaria.repository;


import br.edu.iftm.ds.exemplos.imobiliaria.domain.Corretor;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CorretorRepository extends JpaRepository<Corretor, Integer> {
}
